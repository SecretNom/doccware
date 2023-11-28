from django import forms
from .models import *

class DoceForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields =[
            'name',
            'asignatura',
            'rut'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form_style' ,'required': 'true', 'id':'name', 'placeholder': 'Ingrese el nombre'}),
            'rut': forms.TextInput(attrs={'class': 'form_style', 'required': 'true', 'id': 'rut', 'placeholder': 'Ingrese el Rut con (-)'}),
            'asignatura': forms.CheckboxSelectMultiple(attrs={'class': 'form_style grid grid-cols-2  text-left',  'id': 'asignatura', 'placeholder': 'Ingrese la asignatura'})
        }

class LicenciaForm(forms.ModelForm):
    class Meta:
        model = Licencia
        fields = ['date', 'imagen']