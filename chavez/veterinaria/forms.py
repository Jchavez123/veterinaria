from django import forms
from veterinaria.models import usuario


class usuarioForm(forms.ModelForm):
    class Meta:
        model= usuario
        fields=['nombre', 'apellidos', 'direccion','telefono','email','contraseña','sexo']
        