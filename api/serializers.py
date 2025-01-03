from rest_framework import serializers
from .models import *


class CivilStatusSerializer(serializers.ModelSerializer):
	class Meta:
		model = Civil_Status
		fields = ('nationality_id', 'full_name', 'birth', 'gender',)


class PatientSerializer(serializers.ModelSerializer):
	class Meta:
		model = Patient
		fields = ('nationality_id', 'phone', 'email',)


class HospitalSerializer(serializers.ModelSerializer):
	class Meta:
		model = Hospital
		fields = ('name', 'logo', 'email',)


class MedicalExaminationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Medical_Examination
		fields = ('patient', 'type', 'result', 'note', 'date', 'file', 'stuff',)