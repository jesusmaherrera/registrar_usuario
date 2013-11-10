from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
	username = forms.CharField(max_length=30, min_length=4)
	first_name = forms.CharField(max_length=30, label='Nombre' )
	last_name = forms.CharField(max_length=30, label='Apellido')
	email = forms.EmailField(max_length=75)
	terms = forms.BooleanField(
    error_messages={'required': 'Debes aceptar los terminos y condiciones'},
    label=""
)
	
	class Meta:
		model = User
		fields = ("username", "first_name", "last_name", "email",)