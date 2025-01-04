import django_filters
from django_filters import DateFilter, CharFilter

from api.models import *

class MedicalExaminationFilter(django_filters.FilterSet):
	
	class Meta:
		model = Medical_Examination
		fields = '__all__'
		exclude = ['date', 'id', 'patient', 'report', 'result', 'hospital']
