from django.urls import path
from . import views

urlpatterns = [
	path('dashboard/', views.hospital_dashboard, name='hospital_dashboard'),
	path('patients/', views.hospital_patients, name='hospital_patients'),
	path('patients/national_id/check/', views.h_check_nationality_id, name='h_check_nationality_id'),
	path('patinets/new/<int:nationality_id>/', views.h_add_patient, name='h_add_patient'),
	path('patients/<int:nationality_id>/medical_history/', views.h_patient_history, name='h_patient_history'),
	path('patients/<int:nationality_id>/health_state/update/', views.h_update_health_state, name='h_update_health_state'),
	path('patients/<int:nationality_id>/health_state/history/', views.h_health_state_history, name='h_health_state_history'),
	path('patients/<int:nationality_id>/prescriptions/new/', views.h_add_prescription, name='h_add_prescription'),
	path('patients/<int:nationality_id>/medical_test/new/', views.h_add_medical_test, name='h_add_medical_test'),
	path('patients/<int:nationality_id>/diseases/add/', views.h_add_patient_disease, name='h_add_patient_disease'),
]
