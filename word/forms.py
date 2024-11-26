from django import forms
from .models import Proyecto, Categoria

class FormularioProyecto(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre', 'descripcion', 'imagen','publicar','fecha_creacion', 'categoria']
        
        widgets = {
            'fecha_creacion': forms.DateInput(attrs={'type': 'date'}),
            
        }

class FormularioCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']