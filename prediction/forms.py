from django import forms
from django.contrib.auth.models import User
from prediction.models import RegisterModel, PredictionModel

class RegisterForm(forms.ModelForm):
	class Meta:
		model = RegisterModel
		fields = ["name","email", "phone","address", "tenth", "puc", "degree", "branch"]

class PredictionForm(forms.ModelForm):
    class Meta:
        model = PredictionModel
        fields = ["emailid","technical", "aptitude", "gd", "pi", "tenth", "puc", "degree"]

