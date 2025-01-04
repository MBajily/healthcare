from django.shortcuts import render, redirect
from api.models import *
import datetime
from .forms import *
from .filters import *
from .decorators import allowed_users
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

#================ Export As PDF ======================
# from io import BytesIO
# from django.http import HttpResponse
# from django.template.loader import get_template
# from django.views import View
# from xhtml2pdf import pisa
#=====================================================


#=====================================================
#=================== Dashboard =======================
#=====================================================
#------------------- Dashboard -----------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['ADMIN'])
def dashboard(request):
	main_menu = 'dashboard'
	sub_menu = ''

	hospitals_count = Hospital.hospital.all().count()
	patients_count = Patient.patient.all().count()
	medical_examinations_count = Medical_Examination.objects.all().count()
	recent_hospitals = HospitalProfile.objects.filter(is_active=1).order_by('-date_joined')[:5]
	recent_patients = PatientProfile.objects.order_by('-date_joined')[:5]

	context = {'title':'Dashboard', 'main_menu':main_menu, 
			   'sub_menu':sub_menu, 'hospitals_count':hospitals_count,
			   'patients_count':patients_count, 'medical_examinations_count':medical_examinations_count,
			   'recent_hospitals':recent_hospitals, 'recent_patients':recent_patients}
	
	return render(request, 'ministry/dashboard/dashboard.html', context)
#-----------------------------------------------------
#=====================================================
#=====================================================
#=====================================================


#=====================================================
#================ Medical History ====================
#=====================================================
#---------------- Medical History --------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['ADMIN'])
def medical_history(request, nationality_id):
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
	print(diseases)
	context = {'title':'Medical History', 'main_menu':main_menu, 'diseases':diseases,
			   'sub_menu':sub_menu, 'selected_patient':selected_patient,
			   'medical_examinations':medical_examinations, 
			   'medical_examinations_filter':medical_examinations_filter,
			   'recent_health_state':recent_health_state, 'all_prescriptions':all_prescriptions}
	
	return render(request, 'ministry/medical_history/medical_history.html', context)
#-----------------------------------------------------
#=====================================================
#=====================================================
#=====================================================


#=====================================================
#==================== Hospital =======================
#=====================================================
#------------------- Hospitals -----------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['ADMIN'])
def hospitals(request):
	main_menu = 'hospitals'
	sub_menu = 'all_hospitals'

	all_hospitals = HospitalProfile.objects.filter(is_active=1).all()
	all_hospitals = set(all_hospitals)

	context = {'title':'Hospitals', 'all_hospitals':all_hospitals, 
			   'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'ministry/hospitals/hospitals.html', context)
#-----------------------------------------------------


#-------------------- Add Hospital -------------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['ADMIN'])
def add_hospital(request):
	main_menu = 'hospitals'
	sub_menu = 'add_hospital'
	# groups = Group.objects.order_by('name').all()
	if request.method == 'POST':
		if request.user.check_password(request.POST["admin_password"]):
			email = request.POST["email"]
			new_hospital = Hospital(email=email, password=Patient.objects.make_random_password(length=14))
			if new_hospital:
				new_hospital.save()
				hospital_profile = HospitalProfile.objects.get(user=new_hospital)
				hospital_profile.logo = request.POST["logo"]
				hospital_profile.name = request.POST["name"]
				if hospital_profile:
					hospital_profile.save()
					return redirect('hospitals')
		else:
			return redirect('add_hospital')
	else:
		form = HospitalProfileForm()

	context = {'title':'New Hospital', 'form':form,
			   'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'ministry/hospitals/add_hospital.html', context)
#-----------------------------------------------------

#------------------- Update Hospital -------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['ADMIN'])
def hospital_update(request, hospital_id):
	main_menu = 'hospitals'
	sub_menu = 'all_hospitals'
	
	selected_hospital = Hospital.objects.get(id=hospital_id)
	selected_hospital_profile = HospitalProfile.objects.get(user=selected_hospital)
	hospital_profile_form = HospitalProfileForm(instance=selected_hospital)
	if request.method == 'POST':
		if request.user.check_password(request.POST["admin_password"]):
			selected_hospital_profile.name = request.POST['name']
			selected_hospital_profile.logo = request.FILES['logo']
			if selected_hospital_profile:
				selected_hospital_profile.save()
				return redirect('hospitals')
		else:
			return redirect('hospital_update', hospital_id)

	context = {'title': selected_hospital_profile.name, 'sub_menu':sub_menu,
				'hospital_profile_form':hospital_profile_form, 'main_menu':main_menu,
				'selected_hospital':selected_hospital}

	return render(request, 'ministry/hospitals/hospital_update.html', context)
#-----------------------------------------------------


#----------------- Deactive Hospital -----------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['ADMIN'])
def hospital_deactive(request, hospital_id):
	main_menu = 'hospitals'
	sub_menu = 'all_hospitals'

	selected_hospital = Hospital.objects.get(id=hospital_id)
	selected_hospital_profile = HospitalProfile.objects.get(user=selected_hospital)
	
	if request.method == 'POST':
		if request.user.check_password(request.POST["admin_password"]):
			selected_hospital.is_deleted = True
			selected_hospital_profile.is_deleted = True
			selected_hospital.save()
			selected_hospital_profile.save()
			return redirect('hospitals')
		else:
			return redirect('hospital_deactive', hospital_id)

	context = {'title':'Deactive Hospital', 'item':selected_hospital,
			   'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'ministry/hospitals/hospital_deactive.html', context)
#-----------------------------------------------------


#----------------- Active Hospital -----------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['ADMIN'])
def hospital_active(request, hospital_id):
	main_menu = 'hospitals'
	sub_menu = 'all_hospitals'

	selected_hospital = Hospital.objects.get(id=hospital_id)
	selected_hospital_profile = HospitalProfile.objects.get(user=selected_hospital)
	
	if request.method == 'POST':
		if request.user.check_password(request.POST["admin_password"]):
			selected_hospital.is_deleted = False
			selected_hospital_profile.is_deleted = False
			selected_hospital.save()
			selected_hospital_profile.save()
			return redirect('hospitals')
		else:
			return redirect('hospital_active', hospital_id)

	context = {'title':'Active Hospital', 'item':selected_hospital,
			   'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'ministry/hospitals/hospital_active.html', context)
#-----------------------------------------------------



#=====================================================
#==================== patient ========================
#=====================================================
#------------------- patients ------------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['ADMIN'])
def patients(request):
	main_menu = 'patients'
	sub_menu = 'all_patients'

	all_patients = PatientProfile.objects.all()
	all_patients = set(all_patients)

	context = {'title':'Patients', 'all_patients':all_patients, 
			   'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'ministry/patients/patients.html', context)
#-----------------------------------------------------

#----------------- Delete patient -----------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['ADMIN'])
def patient_delete(request, patient_id):
	main_menu = 'patients'
	sub_menu = 'all_patients'

	selected_civil_status = Civil_Status.objects.get(nationality_id=patient_id)
	selected_patient = Patient.objects.get(civil_status=selected_civil_status)
	
	if request.method == 'POST':
		if request.user.check_password(request.POST["admin_password"]):
			selected_patient.delete()
			return redirect('patients')
		else:
			return redirect('patient_delete', patient_id)

	context = {'title':'Delete Patient', 'item':selected_patient,
			   'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'ministry/patients/patient_delete.html', context)
#-----------------------------------------------------


#-------------- Nationality ID Check -----------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['ADMIN'])
def check_nationality_id(request):
	main_menu = 'patients'
	sub_menu = 'add_patient'
	# groups = Group.objects.order_by('name').all()
	if request.method == 'POST':
		civil_status = Civil_Status.objects.filter(nationality_id=request.POST["nationality_id"]).first()
		if (civil_status is not None):
			if not(PatientProfile.objects.filter(civil_status=civil_status)):
				return redirect('add_patient', civil_status.nationality_id)

	context = {'title':'Check Nationality ID',
			   'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'ministry/patients/check_nationality_id.html', context)
#-----------------------------------------------------


#-------------------- Add patient -------------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['ADMIN'])
def add_patient(request, nationality_id):
	main_menu = 'patients'
	sub_menu = 'add_patient'
	civil_status = Civil_Status.objects.get(nationality_id=nationality_id)
	formset = CivilStatusForm(instance=Civil_Status.objects.get(nationality_id=nationality_id))
	if (civil_status is not None):
		if not(PatientProfile.objects.filter(civil_status=civil_status)):
			if request.method == 'POST':
				if (civil_status is not None):
					if not(PatientProfile.objects.filter(civil_status=civil_status)):
						if request.user.check_password(request.POST["admin_password"]):
							added_patient = Patient(email=request.POST["email"])
							if added_patient:
								added_patient.save()
								patient_profile = PatientProfile.objects.get(user=added_patient)
								patient_profile.photo = request.POST["photo"]
								patient_profile.phone = request.POST["phone"]
								patient_profile.civil_status = civil_status
								patient_profile.save()
								return redirect('patients')
						else:
							return redirect('add_patient', nationality_id)
			else:
				form = PatientProfileForm()

			context = {'title':'New Patient', 'form':form, 'formset':formset,
					   'main_menu':main_menu, 'sub_menu':sub_menu}

			return render(request, 'ministry/patients/add_patient.html', context)
	return redirect('check_nationality_id')
#-----------------------------------------------------


#------------------- Update patient -------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['ADMIN'])
def patient_update(request, nationality_id):
	main_menu = 'patients'
	sub_menu = 'all_patients'
	
	civil_status = Civil_Status.objects.get(nationality_id=nationality_id)
	selected_patient = PatientProfile.objects.get(civil_status=civil_status)
	patient_profile_form = PatientProfileForm(instance=selected_patient)
	if request.method == 'POST':
		if request.user.check_password(request.POST["admin_password"]):
			phone = request.POST['phone']
			
			selected_patient.phone = phone
			if selected_patient:
				selected_patient.save()
				return redirect('patients')
		else:
			return redirect('patient_update', nationality_id)

	context = {'title': selected_patient.civil_status.full_name, 'sub_menu':sub_menu,
				'main_menu':main_menu, 'patient_profile_form':patient_profile_form,
				'selected_patient':selected_patient, 'civil_status':civil_status}

	return render(request, 'ministry/patients/patient_update.html', context)
#-----------------------------------------------------



#=====================================================
#===================== Charts ========================
#=====================================================
#----------------- Patients Chart --------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['ADMIN'])
def patients_chart(request):
	data = []

	for d in (datetime.date.today() - datetime.timedelta(days=x) for x in reversed(range(0,30))):
		patients_count = Patient.patient.filter(date_joined=d.strftime("%Y-%m-%d")).all().count()
		if patients_count:
			data.append({'{}'.format(d.strftime("%b, %d")): patients_count})
		else:
			data.append({'{}'.format(d.strftime("%b, %d")): 0})
	
	return JsonResponse(data, safe=False)
#-----------------------------------------------------


#----------- Medical Examinations Chart --------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['ADMIN'])
def medical_examinations_chart(request):
	data = []

	for d in (datetime.date.today() - datetime.timedelta(days=x) for x in reversed(range(0,30))):
		medical_examinations_count = Medical_Examination.objects.filter(date=d.strftime("%Y-%m-%d")).all().count()
		if medical_examinations_count:
			data.append({'{}'.format(d.strftime("%b, %d")): medical_examinations_count})
		else:
			data.append({'{}'.format(d.strftime("%b, %d")): 0})
	
	return JsonResponse(data, safe=False)
#-----------------------------------------------------



#=====================================================
#============== Basic Health State ===================
#=====================================================

#--------------- Add Health State --------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['ADMIN'])
def update_health_state(request, nationality_id):
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
			return redirect('medical_history', nationality_id)
	else:
		health_state = Basic_Health_State.objects.filter(patient=selected_patient.user).order_by('-date').first()
		form = BasicHealthStateForm(instance=health_state)

	context = {'title':'Update Basic Health State', 'form':form,
			   'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'ministry/medical_history/basic_health_state.html', context)
#-----------------------------------------------------


#------------ Add Health State History ---------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['ADMIN'])
def health_state_history(request, nationality_id):
	main_menu = 'patients'
	sub_menu = 'all_patients'

	civil_status = Civil_Status.objects.get(nationality_id=nationality_id)
	selected_patient = PatientProfile.objects.get(civil_status=civil_status)

	health_state = Basic_Health_State.objects.filter(patient=selected_patient.user).order_by('-date')

	context = {'title':'Health State History', 'health_state':health_state,
			   'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'ministry/medical_history/basic_health_state_history.html', context)
#-----------------------------------------------------

#=====================================================
#=================== Prescription ====================
#=====================================================

#----------------- Add Prescription ------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['ADMIN'])
def add_prescription(request, nationality_id):
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
			return redirect('medical_history', nationality_id)
	else:
		form = PrescriptionForm()

	context = {'title':'Add Prescription', 'form':form,
			   'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'ministry/medical_history/add_prescription.html', context)
#-----------------------------------------------------

#=====================================================
#=============== Medical Examinations ================
#=====================================================

#----------------- Add Medical Test ------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['ADMIN'])
def add_medical_test(request, nationality_id):
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
			return redirect('medical_history', nationality_id)
	else:
		form = MedicalExaminationForm()

	context = {'title':'Add Medical Test', 'form':form,
			   'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'ministry/medical_history/add_medical_test.html', context)
#-----------------------------------------------------

#=====================================================
#================= Patient Disease ===================
#=====================================================

#----------------- Add Prescription ------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['ADMIN'])
def add_patient_disease(request, nationality_id):
	main_menu = 'patients'
	sub_menu = 'all_patients'

	civil_status = Civil_Status.objects.get(nationality_id=nationality_id)
	selected_patient = PatientProfile.objects.get(civil_status=civil_status)
	old_diseases = Patient_Disease.objects.filter(patient=selected_patient.user).all()
	old_diseases = [d.id for d in old_diseases]
	diseases = Disease.objects.all()
	print(old_diseases)
	if request.method == 'POST':
		selected_diseases = request.POST.getlist('diseases')
		for d in selected_diseases:
			disease = Disease.objects.get(id=d)
			patient_disease = Patient_Disease(patient=selected_patient.user, disease=disease)
			patient_disease.save()
		
		return redirect('medical_history', nationality_id)

	context = {'title':'Update Diseases', 'diseases':diseases, 'old_diseases':old_diseases,
			   'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'ministry/medical_history/add_disease.html', context)
#-----------------------------------------------------