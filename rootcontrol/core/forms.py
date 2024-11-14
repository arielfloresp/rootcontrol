from django import forms
from .models import Datacenter

class DatacenterForm(forms.ModelForm):
    class Meta:
        model = Datacenter
        fields = '__all__'  # Esto incluirá todos los campos del modelo