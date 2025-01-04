from django.urls import path
from . import views

urlpatterns = [
	path('history/', views.patient_history, name='patient_history'),
]
