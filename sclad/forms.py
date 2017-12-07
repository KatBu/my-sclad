from django import forms
from django.forms import ModelForm
from .models import Tovar
from .models import ScladTov
from django.contrib import auth

class TovarForm(ModelForm):
	class Meta:
		model = Tovar
		fields = ['full_name', 'category']

class ScladTovForm(ModelForm):
	class Meta:
		model = ScladTov
		fields = ['mytovars','srokmes', 'srokgod', 'kol']
