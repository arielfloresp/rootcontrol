from django import forms
from .models import Datacenter
from .models import Logbook

class DatacenterForm(forms.ModelForm):
    class Meta:
        model = Datacenter
        fields = '__all__'  # Esto incluirá todos los campos del modelo


# forms.py
from django import forms
from .models import Logbook

class LogbookForm(forms.ModelForm):
    class Meta:
        model = Logbook
        fields = ['bitacora']  # Solo mostramos el campo que el usuario debe llenar
