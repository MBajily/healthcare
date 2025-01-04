# import os
# import secrets
from django.shortcuts import render
from api.models import *
from ministry.filters import *
from ministry.decorators import allowed_users
from django.contrib.auth.decorators import login_required
# # Create your views here.



#=====================================================
#================ Medical History ====================
#=====================================================
#---------------- Medical History --------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['PATIENT'])
def patient_history(request):
	main_menu = 'history'
	sub_menu = 'history'

	selected_patient = PatientProfile.objects.filter(user=request.user).first()
	medical_examinations = Medical_Examination.objects.filter(patient=selected_patient.user).order_by('-date')
	medical_examinations_filter = MedicalExaminationFilter(request.GET, queryset=medical_examinations)
	medical_examinations = medical_examinations_filter.qs.order_by('-date')
	recent_health_state = Basic_Health_State.objects.filter(patient=selected_patient.user).order_by('-date').first()
	all_prescriptions = Prescription.objects.filter(patient=selected_patient.user).order_by('-date')


	context = {'title':'Medical History', 'main_menu':main_menu, 
			   'sub_menu':sub_menu, 'selected_patient':selected_patient,
			   'medical_examinations':medical_examinations, 
			   'medical_examinations_filter':medical_examinations_filter,
			   'recent_health_state':recent_health_state, 
			   'all_prescriptions':all_prescriptions}
	
	return render(request, 'patient/patient_history.html', context)
#-----------------------------------------------------
#=====================================================
#=====================================================
#=====================================================