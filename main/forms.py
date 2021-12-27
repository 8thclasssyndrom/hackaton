from django import forms
from django.forms import widgets

from .models import *


class CreateCharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = '__all__'


class UpdateCharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = '__all__'
