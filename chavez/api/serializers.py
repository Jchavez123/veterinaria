from rest_framework import serializers
#inmportando
from veterinaria.models import usuario,tipoV,mascota,historia,controlv


#inmpotando nmodelo de la bd
class usuarioSerializer(serializers.ModelSerializer):
 class Meta:
    model = usuario
    fields = ['nombre', 'apellidos', 'direccion','telefono','email','contraseña','sexo']

class tipoVSerializer(serializers.ModelSerializer):
    class Meta:
        model = tipoV
        fields = ['nombre', 'descripcion']

class mascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = mascota
        fields = ['nombre', 'especie', 'raza','sexo','fechaN','color','observaciones','carnet']

class historiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = historia
        fields = ['fecha', 'hora', 'motivo','diagnostico','Tratamiento','temperatura','peso','pulso','respiracion','observaciones']


class controlvSerializer(serializers.ModelSerializer):
    class Meta:
        model = controlv
        fields = ['fechaA', 'observacion', 'notificar']










