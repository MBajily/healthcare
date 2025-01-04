from django.shortcuts import render, redirect
from api.models import *
from ministry.filters import *
from ministry.decorators import allowed_users
from django.contrib.auth.decorators import login_required
# # Create your views here.
from ministry.forms import *

#=====================================================
#=================== Dashboard =======================
#=====================================================
#------------------- Dashboard -----------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['HOSPITAL'])
def hospital_dashboard(request):
	main_menu = 'dashboard'
	sub_menu = ''

	hospitals_count = Hospital.hospital.all().count()
	hospital_patient = Hospital_Patient.objects.filter(hospital=request.user)
	patients_count = hospital_patient.count()
	medical_examinations_count = Medical_Examination.objects.all().count()
	recent_hospitals = HospitalProfile.objects.filter(is_active=1).order_by('-date_joined')[:5]
	patients_id_list = [ patient.id for patient in hospital_patient]
	patients = Patient.patient.filter(id__in=patients_id_list)
	recent_patients = PatientProfile.objects.filter(user__in=patients).order_by('-date_joined')[:5]

	context = {'title':'Dashboard', 'main_menu':main_menu, 
			   'sub_menu':sub_menu, 'hospitals_count':hospitals_count,
			   'patients_count':patients_count, 'medical_examinations_count':medical_examinations_count,
			   'recent_hospitals':recent_hospitals, 'recent_patients':recent_patients}
	
	return render(request, '', context)
#-----------------------------------------------------
#=====================================================
#=====================================================
#=====================================================


#=====================================================
#================ Medical History ====================
#=====================================================
#---------------- Medical History --------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['HOSPITAL'])
def h_patient_history(request, nationality_id):
	main_menu = 'patinets'
	sub_menu = 'all_patients'

	civil_status = Civil_Status.objects.get(nationality_id=nationality_id)
	selected_patient = PatientProfile.objects.filter(civil_status=civil_status).first()
	medical_examinations = Medical_Examination.objects.filter(patient=selected_patient.user).order_by('-date')
	medical_examinations_filter = MedicalExaminationFilter(request.GET, queryset=medical_examinations)
	medical_examinations = medical_examinations_filter.qs.order_by('-date')
	recent_health_state = Basic_Health_State.objects.filter(patient=selected_patient.user).order_by('-date').first()
	all_prescriptions = Prescription.objects.filter(patient=selected_patient.user).order_by('-date')
	diseases = Patient_Disease.objects.filter(patient=selected_patient.user).all()

	context = {'title':'Medical History', 'main_menu':main_menu, 'diseases':diseases,
			   'sub_menu':sub_menu, 'selected_patient':selected_patient,
			   'medical_examinations':medical_examinations, 
			   'medical_examinations_filter':medical_examinations_filter,
			   'recent_health_state':recent_health_state, 'all_prescriptions':all_prescriptions}
	
	return render(request, '', context)
#-----------------------------------------------------
#=====================================================
#=====================================================
#=====================================================


#=====================================================
#=================== Dashboard =======================
#=====================================================
#------------------- Dashboard -----------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['HOSPITAL'])
def hospital_patients(request):
	main_menu = 'patients'
	sub_menu = 'all_patients'

	hospital_patient_list = Hospital_Patient.objects.filter(hospital=request.user)
	hospital_patient_list = [ patient.patient.id for patient in hospital_patient_list]
	patients = Patient.objects.filter(id__in=hospital_patient_list).all()
	all_patients = PatientProfile.objects.filter(user__in=patients)
	all_patients = set(all_patients)

	context = {'title':'Patients', 'all_patients':all_patients, 'hospital_patient_list':hospital_patient_list,
			   'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, '', context)
#-----------------------------------------------------
#=====================================================
#=====================================================
#=====================================================


#=====================================================
#================== Add Patient ======================
#=====================================================
#-------------- Nationality ID Check -----------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['HOSPITAL'])
def h_check_nationality_id(request):
	main_menu = 'patients'
	sub_menu = 'add_patient'
	# groups = Group.objects.order_by('name').all()

	if request.method == 'POST':
		civil_status = Civil_Status.objects.filter(nationality_id=request.POST["nationality_id"]).first()
		patient_profile = PatientProfile.objects.filter(civil_status=civil_status).first()
		if (civil_status is not None) and not(patient_profile):
				return redirect('h_add_patient', civil_status.nationality_id)

		if (civil_status is not None) and (patient_profile):
				related_hospital = Hospital_Patient(hospital=request.user, patient=patient_profile.user)
				related_hospital.save()
				return redirect('h_patient_history', civil_status.nationality_id)
		


	context = {'title':'Check Nationality ID',
			   'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, '', context)
#-----------------------------------------------------


#------------------ Add patient ----------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['HOSPITAL'])
def h_add_patient(request, nationality_id):
	main_menu = 'patients'
	sub_menu = 'add_patient'
	civil_status = Civil_Status.objects.get(nationality_id=nationality_id)
	formset = CivilStatusForm(instance=Civil_Status.objects.get(nationality_id=nationality_id))
	if (civil_status is not None) and not(PatientProfile.objects.filter(civil_status=civil_status)):
		if request.method == 'POST':
			if (civil_status is not None) and not(PatientProfile.objects.filter(civil_status=civil_status)):
				added_patient = Patient(email=request.POST["email"])
				if added_patient:
					added_patient.save()
					patient_profile = PatientProfile.objects.get(user=added_patient)
					patient_profile.photo = request.POST["photo"]
					patient_profile.phone = request.POST["phone"]
					patient_profile.civil_status = civil_status
					patient_profile.save()
					related_hospital = Hospital_Patient(hospital=request.user, patient=added_patient)
					related_hospital.save()

					return redirect('h_patient_history', civil_status.nationality_id)
		else:
			form = PatientProfileForm()

		context = {'title':'New Patient', 'form':form, 'formset':formset,
				   'main_menu':main_menu, 'sub_menu':sub_menu}

		return render(request, '', context)
	return redirect('check_nationality_id')
#-----------------------------------------------------
#=====================================================
#=====================================================
#=====================================================


#=====================================================
#============== Basic Health State ===================
#=====================================================
#-------------- Update Health State ------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['HOSPITAL'])
def h_update_health_state(request, nationality_id):
	main_menu = 'patients'
	sub_menu = 'all_patients'

	civil_status = Civil_Status.objects.get(nationality_id=nationality_id)
	selected_patient = PatientProfile.objects.get(civil_status=civil_status)

	if request.method == 'POST':
		heart_rate = request.POST['heart_rate']
		oxygen_saturation = request.POST['oxygen_saturation']
		body_temperature = request.POST['body_temperature']
		glucose_level = request.POST['glucose_level']
		health_state = Basic_Health_State(patient=selected_patient.user, heart_rate=heart_rate,
										  oxygen_saturation=oxygen_saturation, body_temperature=body_temperature,
										  glucose_level=glucose_level)
		if health_state:
			health_state.save()
			return redirect('h_patient_history', nationality_id)
	else:
		health_state = Basic_Health_State.objects.filter(patient=selected_patient.user).order_by('-date').first()
		form = BasicHealthStateForm(instance=health_state)

	context = {'title':'Update Basic Health State', 'form':form,
			   'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, '', context)
#-----------------------------------------------------


#------------ Add Health State History ---------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['HOSPITAL'])
def h_health_state_history(request, nationality_id):
	main_menu = 'patients'
	sub_menu = 'all_patients'

	civil_status = Civil_Status.objects.get(nationality_id=nationality_id)
	selected_patient = PatientProfile.objects.get(civil_status=civil_status)

	health_state = Basic_Health_State.objects.filter(patient=selected_patient.user).order_by('-date')

	context = {'title':'Health State History', 'health_state':health_state,
			   'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, '', context)
#-----------------------------------------------------

#=====================================================
#=================== Prescription ====================
#=====================================================
#----------------- Add Prescription ------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['HOSPITAL'])
def h_add_prescription(request, nationality_id):
	main_menu = 'patients'
	sub_menu = 'all_patients'

	civil_status = Civil_Status.objects.get(nationality_id=nationality_id)
	selected_patient = PatientProfile.objects.get(civil_status=civil_status)

	if request.method == 'POST':
		start_date = request.POST['start_date']
		end_date = request.POST['end_date']
		type = request.POST['type']
		name = request.POST['name']
		note = request.POST['note']
		prescription = Prescription(patient=selected_patient.user, start_date=start_date,
									end_date=end_date, type=type,
									name=name, note=note)
		if prescription:
			prescription.save()
			return redirect('h_patient_history', nationality_id)
	else:
		form = PrescriptionForm()

	context = {'title':'Add Prescription', 'form':form,
			   'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, '', context)
#-----------------------------------------------------


#=====================================================
#================= Patient Disease ===================
#=====================================================

#----------------- Add Prescription ------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['HOSPITAL'])
def h_add_patient_disease(request, nationality_id):
	main_menu = 'patients'
	sub_menu = 'all_patients'

	civil_status = Civil_Status.objects.get(nationality_id=nationality_id)
	selected_patient = PatientProfile.objects.get(civil_status=civil_status)
	old_diseases = Patient_Disease.objects.filter(patient=selected_patient.user).all()
	old_diseases = [d.disease.id for d in old_diseases]
	diseases = Disease.objects.all()
	print(old_diseases)
	if request.method == 'POST':
		selected_diseases = request.POST.getlist('diseases')
		for d in old_diseases:
			if str(d) not in selected_diseases:
				disease = Disease.objects.get(id=d)
				patient_disease = Patient_Disease.objects.get(disease=disease)
				patient_disease.delete()
		for d in selected_diseases:
			if int(d) not in old_diseases:
				disease = Disease.objects.get(id=d)
				patient_disease = Patient_Disease(patient=selected_patient.user, disease=disease)
				patient_disease.save()
		return redirect('h_patient_history', nationality_id)

	context = {'title':'Update Diseases', 'diseases':diseases, 'old_diseases':old_diseases,
			   'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, '', context)
#-----------------------------------------------------


#=====================================================
#=============== Medical Examinations ================
#=====================================================

#----------------- Add Medical Test ------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['HOSPITAL'])
def h_add_medical_test(request, nationality_id):
	main_menu = 'patients'
	sub_menu = 'all_patients'

	civil_status = Civil_Status.objects.get(nationality_id=nationality_id)
	selected_patient = PatientProfile.objects.get(civil_status=civil_status)

	if request.method == 'POST':
		type = request.POST['type']
		report = request.POST['report']
		result = request.FILES['result']
		medical_test = Medical_Examination(patient=selected_patient.user, type=type,
										result=result, report=report)
		if medical_test:
			medical_test.save()
			return redirect('h_patient_history', nationality_id)
	else:
		form = MedicalExaminationForm()

	context = {'title':'Add Medical Test', 'form':form,
			   'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, '', context)
#-----------------------------------------------------