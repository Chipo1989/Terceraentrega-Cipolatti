from django import forms
from .models import Tarea, Desarrollo, EstadoTarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['nombre', 'descripcion', 'estado']
        
class DesarrolloForm(forms.ModelForm):
    class Meta:
        model = Desarrollo
        fields = ['tarea', 'detalles', 'fecha_desarrollo']

class EstadoTareaForm(forms.ModelForm):
    class Meta:
        model = EstadoTarea
        fields = ['nombre']

class TareaSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False)