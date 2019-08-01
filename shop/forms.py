from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import Profile

def validate_ten(value):
    if len(value) < 10:
        raise ValidationError(
            _('%(value)s is not a 10 digit number'),
            params={'value': value},
        )

def validate_phone(value):
	test = Profile.objects.get(phone = value)
	if test:
		raise ValidationError(
            _('%(value)s Not Unique'),
            params={'value': value},
        )


class SignUpForm (UserCreationForm):
	first_name = forms.CharField(max_length=100,required=True)
	last_name = forms.CharField(max_length=100,required=True)
	email = forms.EmailField(max_length=254,help_text='',required=True)
	phone = forms.CharField(max_length=15,help_text='form: 7853701281',required=True,validators=[validate_ten,validate_phone])
	pickup = forms.CharField(max_length=254,help_text='Default address for student pickup option',required=False)
	
	class Meta:
		model = User
		fields= ('username','password1','password2','first_name','last_name','email','phone',)