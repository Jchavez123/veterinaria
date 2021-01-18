from django.contrib import admin

from veterinaria.models import usuario
from veterinaria.models import tipoV
from veterinaria.models import  mascota
from veterinaria.models import historia
from veterinaria.models import  doctor
from veterinaria.models import controlv
from veterinaria.models import horario
from veterinaria.models import tipocita
from veterinaria.models import reservacita

# Register your models here.
admin.site.register(usuario)
admin.site.register(tipoV)
admin.site.register(mascota)
admin.site.register(historia)
admin.site.register(doctor)
admin.site.register(controlv)
admin.site.register(horario)
admin.site.register(tipocita)
admin.site.register(reservacita)
