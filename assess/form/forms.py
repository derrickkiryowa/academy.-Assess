from django.forms import ModelForm
from django import forms 
from .models import *
from django.core.exceptions import ValidationError


class StudentForm(forms.ModelForm):
  class Meta:

    model = Student
    fields = '__all__'
    widgets = {
            'first_name':forms.TextInput(attrs={ 'required':'required'}),
            'last_name':forms.TextInput(attrs={ 'required':'required'}),
            'course':forms.Select(attrs={ 'required':'required'}),
            'entry_scheme':forms.Select(attrs={ 'required':'required'}),
            'intake':forms.Select(attrs={ 'required':'required'}),
            'sponsorship':forms.Select(attrs={ 'required':'required'}),
            'gender':forms.RadioSelect(attrs={ 'required':'required'}),
            'date_of_birth':forms.DateInput(attrs={ 'required':'required'}),
            'residence':forms.TextInput(attrs={ 'required':'required'}),
        }