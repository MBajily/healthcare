from django import forms 
from api.models import *

from django.contrib.auth.forms import UserCreationForm


# =====================================================
# =============== Registertion Form ===================
# =====================================================
class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']


#=====================================================
#===================== Kin Form ======================
#=====================================================
class CivilStatusForm(forms.ModelForm):
	class Meta:
		model = Civil_Status
		fields = ['nationality_id', 'full_name', 'birth', 'gender']
		widgets = {
			'nationality_id': forms.TextInput(attrs={'name':'nationality_id', 'class': 'form-control', 'id': 'inputName', 'required': 'True', 'disabled': 'True'}),
			'full_name': forms.TextInput(attrs={'name':'full_name', 'class': 'form-control', 'id': 'inputName', 'placeholder': '', 'required': 'True', 'disabled': 'True'}),
			'birth': forms.TextInput(attrs={'name':'birth', 'class': 'form-control', 'id': 'inputName', 'required': 'True', 'disabled': 'True'}),
			'gender': forms.TextInput(attrs={'name':'gender', 'class': 'form-control', 'id': 'inputName', 'required': 'True', 'disabled': 'True'}),
		}


#=====================================================
#=================== Patient Form ====================
#=====================================================
class PatientProfileForm(forms.ModelForm):
	class Meta:
		model = PatientProfile
		fields = ['phone', 'photo']
		widgets = {
			'phone': forms.TextInput(attrs={'name':'phone', 'class': 'form-control mb-5', 'id': 'inputName', 'required': 'True'}),
			'photo': forms.FileInput(attrs={'name':'photo', 'id':"input-file-to-destroy", 'class':"dropify mb-5", 'data-allowed-formats':"portrait square", 'data-max-file-size':"2M", 'data-max-height':"2000", 'required':'True'})
			# 'email': forms.EmailInput(attrs={'name':'email', 'class':"form-control", 'id':"inputEmail", 'placeholder':"Email", 'data-error':"Bruh, that email address is invalid", 'required':'True'}),
		}


#=====================================================
#===================== Kin Form ======================
#=====================================================
class KinForm(forms.ModelForm):
	class Meta:
		model = Kin
		fields = ['full_name', 'address', 'relationship', 'phone', 'email']
		widgets = {
			'full_name': forms.TextInput(attrs={'name':'first_name', 'class': 'form-control', 'id': 'inputName', 'required': 'True'}),
			'address': forms.Textarea(attrs={'class': 'form-control', 'id': 'inputName', 'placeholder': '', 'required': 'True'}),
			'relationship': forms.Select(attrs={'name':'relationship', 'class': "form-select form-select-lg mb-3", 'required': 'True'}),
			'phone': forms.TextInput(attrs={'name':'last_name', 'class': 'form-control', 'id': 'inputName', 'required': 'True'}),
			'email': forms.EmailInput(attrs={'name':'email', 'class':"form-control", 'id':"inputEmail", 'placeholder':"Email", 'data-error':"Bruh, that email address is invalid", 'required':'True'}),
		}


#=====================================================
#================== Hospital Form ====================
#=====================================================
class HospitalForm(forms.ModelForm):
	class Meta:
		model = Hospital
		fields = ['email']
		widgets = {
			# 'name': forms.TextInput(attrs={'name':'name', 'class': 'form-control', 'id': 'inputName', 'required': 'True'}),
			'email': forms.EmailInput(attrs={'name':'email', 'class':"form-control", 'id':"inputEmail", 'placeholder':"Email", 'data-error':"Bruh, that email address is invalid", 'required':'True'}),
			# 'logo': forms.FileInput(attrs={'name':'logo', 'id':"input-file-to-destroy", 'class':"dropify", 'data-allowed-formats':"portrait square", 'data-max-file-size':"2M", 'data-max-height':"2000", 'required':'True'})
		}

class HospitalProfileForm(forms.ModelForm):
	class Meta:
		model = HospitalProfile
		fields = ['name', 'logo']
		widgets = {
			'name': forms.TextInput(attrs={'name':'name', 'class': 'form-control', 'id': 'inputName', 'required': 'True'}),
			# 'email': forms.EmailInput(attrs={'name':'email', 'class':"form-control", 'id':"inputEmail", 'placeholder':"Email", 'data-error':"Bruh, that email address is invalid", 'required':'True'}),
			'logo': forms.FileInput(attrs={'name':'logo', 'id':"input-file-to-destroy", 'class':"dropify", 'data-allowed-formats':"portrait square", 'data-max-file-size':"2M", 'data-max-height':"2000", 'required':'True'})
		}



#=====================================================
#============ Medical Examination Form ===============
#=====================================================
class MedicalExaminationForm(forms.ModelForm):
	class Meta:
		model = Medical_Examination
		fields = ['type', 'report', 'result']
		widgets = {
			'type': forms.Select(attrs={'name':'type', 'class': "form-select form-select-lg mb-3", 'required': 'True'}),
			'report': forms.Textarea(attrs={'name':'report', 'class': 'form-control', 'id': 'inputName', 'placeholder': '', 'required': 'False'}),
			'result': forms.FileInput(attrs={'name':'result', 'id':"input-file-to-destroy", 'class':"dropify", 'required':'True'})
		}		


#=====================================================
#============ Basic Health State Form ===============
#=====================================================
class BasicHealthStateForm(forms.ModelForm):
	class Meta:
		model = Basic_Health_State
		fields = ['heart_rate', 'oxygen_saturation', 'body_temperature', 'glucose_level']
		widgets = {
			'type': forms.Select(attrs={'name':'type', 'class': "form-select form-select-lg mb-3", 'required': 'True'}),
			'heart_rate': forms.TextInput(attrs={'name':'heart_rate', 'class': 'form-control', 'id': 'inputName', 'placeholder': '', 'required': 'False'}),
			'oxygen_saturation': forms.TextInput(attrs={'name':'oxygen_saturation', 'class': 'form-control', 'id': 'inputName', 'placeholder': '', 'required': 'False'}),
			'body_temperature': forms.TextInput(attrs={'name':'body_temperature', 'class': 'form-control', 'id': 'inputName', 'placeholder': '', 'required': 'False'}),
			'glucose_level': forms.TextInput(attrs={'name':'glucose_level', 'class': 'form-control', 'id': 'inputName', 'placeholder': '', 'required': 'False'}),
		}		


#=====================================================
#================= Prescription Form =================
#=====================================================
class PrescriptionForm(forms.ModelForm):
	class Meta:
		model = Prescription
		fields = ['type', 'name', 'start_date', 'end_date', 'note']
		widgets = {
			'type': forms.Select(attrs={'name':'type', 'class': "form-select form-select-lg mb-5", 'required': 'True'}),
			'note': forms.Textarea(attrs={'name':'note', 'class': 'form-control mb-5', 'id': 'inputName', 'placeholder': '', 'required': 'True'}),
			'name': forms.TextInput(attrs={'name':'name', 'class': 'form-control mb-5', 'id': 'inputName', 'placeholder': '', 'required': 'False'}),
			'start_date': forms.TextInput(attrs={'name':'start_date', 'class':"form-control mb-5", 'placeholder':"yyyy-mm-dd", 'id':"datepicker", 'data-date-format':"yyyy-mm-dd"}),
			'end_date': forms.TextInput(attrs={'name':'end_date', 'class':"form-control mb-5", 'placeholder':"yyyy-mm-dd", 'id':"datepicker", 'data-date-format':"yyyy-mm-dd"}),
		}	