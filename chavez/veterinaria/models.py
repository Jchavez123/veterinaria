from django.db import models
from datetime import date

# Create your models here.
class usuario(models.Model):
     
    
      nombre=models.CharField( max_length = 100, verbose_name = 'nombre') 
      apellidos=models.CharField( max_length = 100, verbose_name = 'apellidos')   
      direccion=models.CharField( max_length = 100, verbose_name = 'direccion')  
      telefono=models.CharField( max_length = 500, verbose_name = 'telefono')  
      email=models.EmailField(max_length = 100, verbose_name = 'email')
      contraseña=models.CharField(max_length = 100, verbose_name = 'contraseña')
      sexo=models.CharField( max_length = 2, verbose_name = 'sexo')

      created_on=models.DateTimeField(auto_now_add=True)
      
      class Meta:
        ordering = ['created_on']
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'
        def __str__(self):
           return self.nombre
       

#relacionado 
class mascota(models.Model):

    nombre=models.CharField(max_length = 100, verbose_name = 'nombre')
    especie=models.CharField(max_length = 100, verbose_name = 'nombre')
    raza=models.CharField(max_length = 100, verbose_name = 'raza')
    sexo=models.CharField(max_length = 2, verbose_name = 'sexo')
    fechaN=models.CharField(max_length = 50, verbose_name = 'fechaN')
    color=models.CharField(max_length = 100, verbose_name = 'color')
    observaciones=models.TextField(verbose_name='observaciones')
    carnet=models.CharField( max_length=50,blank=True,null=True,verbose_name='carnet')
    created_on=models.DateTimeField(auto_now_add=True)
    image = models.ImageField("Imagen", upload_to='restaurant'
     , blank=True)
    #foto
    usuario= models.ForeignKey('usuario', on_delete=models.CASCADE)


    class Meta:
        ordering = ['created_on']
        verbose_name = 'mascota'
        verbose_name_plural = 'mascotas'


        def __str__(self): # self -> this
            return 'R:{} -> L: {}'.format(self.usuario.nombre, self.nombre)




class historia(models.Model):
    
    fecha=models.CharField(max_length = 10, verbose_name = 'fecha')
    diagnostico=models.CharField(max_length = 100, verbose_name = 'diagnostico')
    Tratamiento=models.CharField(max_length = 100, verbose_name = 'Tratamiento')
    temperatura=models.CharField(max_length = 100, verbose_name = 'temperatura')
    peso=models.CharField( max_length = 100, verbose_name = 'peso')
    pulso=models.CharField( max_length = 100, verbose_name = 'pulso')
    respiracion=models.CharField( max_length = 100, verbose_name = 'Tratamiento')
    observaciones=models.TextField(verbose_name='observaciones')
    
    created_on=models.DateTimeField(auto_now_add=True)
    mascota = models.ForeignKey('mascota', on_delete=models.CASCADE)

    class Meta:
            ordering = ['created_on']
            verbose_name = 'historia'
            verbose_name_plural = 'historias'


            def __str__(self): # self -> this
             return 'R:{} -> L: {}'.format(self.mascota.fecha, self.fecha)


class doctor(models.Model):

     nombre=models.CharField( max_length = 100, verbose_name = 'nombre') 
     apellidos=models.CharField( max_length = 100, verbose_name = 'apellidos')   
     direccion=models.CharField( max_length = 100, verbose_name = 'direccion')  
     telefono=models.CharField( max_length = 500, verbose_name = 'telefono')  
     email=models.EmailField(max_length = 100, verbose_name = 'email')
     created_on=models.DateTimeField(auto_now_add=True)
     descripcion=models.TextField(verbose_name='descrpcion')

     class Meta:
        ordering = ['created_on']
        verbose_name = 'veterinario'
        verbose_name_plural = 'veterinarios'
        def __str__(self):
           return self.nombre



class horario(models.Model):
    horainicio=models.CharField( max_length=50,verbose_name='horainicio')
    horafin=models.CharField( max_length=50, verbose_name='horafin')
    created_on=models.DateTimeField(auto_now_add=True)
    doctor = models.ForeignKey('doctor', on_delete=models.CASCADE)


    class Meta:
        ordering = ['created_on']
        verbose_name = 'horario'
        verbose_name_plural = 'horarios'
        
        def __str__(self):

              return 'R:{} -> L: {}'.format(self.doctor.nombre, self.nombre)



class tipocita(models.Model):
    nombre:models.CharField( max_length=50,verbose_name='nombre')
    descripcion:models.TextField(verbose_name='descripcion')
    created_on=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']
        verbose_name = 'tipocita'
        verbose_name_plural = 'tipocitas'
        def __str__(self):
           return self.nombre



 

class tipoV (models.Model):   
    
    nombre=models.CharField( max_length = 100, verbose_name = 'nombre')
    descripcion=models.TextField(verbose_name='descripcion')
    created_on=models.DateTimeField(auto_now_add=True)

    class Meta:
            ordering = ['created_on']
            verbose_name = 'tipoV'
            verbose_name_plural = 'tipoVs'

            def __str__(self):
             return self.nombre



class controlv(models.Model):
    
    fechaA=models.CharField(max_length = 100, verbose_name = 'fechaA')
    observacion=models.TextField( verbose_name = 'observaciones')
    notificar=models.CharField(max_length=50)
    created_on=models.DateTimeField(auto_now_add=True)

    mascota = models.ForeignKey('mascota', on_delete=models.CASCADE)
    tipoV = models.ForeignKey('tipoV', on_delete=models.CASCADE)


    class Meta:
            ordering = ['created_on']
            verbose_name = 'controlv'
            verbose_name_plural = 'controlv'


            def __str__(self): # self -> this
             return 'R:{} -> L: {}'.format(self.mascota.nombre, self.nombre)
             return 'R:{} -> L: {}'.format(self.tipoV.nombre, self.nombre)

class reservacita (models.Model):
    
    fecha=models.CharField(max_length = 10, verbose_name = 'fecha')
    inicio=models.CharField(max_length = 60, verbose_name = 'inicio')
    fin=models.CharField(max_length = 60, verbose_name = 'fin')
    mascota = models.ForeignKey('mascota', on_delete=models.CASCADE)
    tipocita = models.ForeignKey('tipocita', on_delete=models.CASCADE)
    created_on=models.DateTimeField(auto_now_add=True)
    horario = models.ForeignKey('horario', on_delete=models.CASCADE)


    class Meta:
            ordering = ['created_on']
            verbose_name = 'cita'
            verbose_name_plural = 'citas'


            def __str__(self): # self -> this
              return 'R:{} -> L: {}'.format(self.mascota.nombre, self.nombre)
              return 'R:{} -> L: {}'.format(self.tipocita.nombre, self.nombre)
              return 'R:{} -> L: {}'.format(self.horario.nombre, self.nombre)







