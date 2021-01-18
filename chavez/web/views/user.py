#from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
#from veterinaria.models import usuario

class userhomeView(View):
    '''
    Vista de la pagina Home
    '''
    template_name = 'user/home-usuario.html'

    def get(self, request):
        return render(request, self.template_name, {})

class userinternadoView(View):
    '''
    Vista de la pagina Home
    '''
    template_name = 'user/internado-usuario.html'

    def get(self, request):
        return render(request, self.template_name, {})

class usermascotaView(View):
    '''
    Vista de la pagina Home
    '''
    template_name = 'user/mascota-usuario.html'

    def get(self, request):
        return render(request, self.template_name, {})

class usermascotahistoriaView(View):
    '''
    Vista de la pagina Home
    '''
    template_name = 'user/mascota-historial.html'

    def get(self, request):
        return render(request, self.template_name, {})

class usertarjetaView(View):
    '''
    Vista de la pagina Home
    '''
    template_name = 'user/tarjeta-vacuna.html'

    def get(self, request):
        return render(request, self.template_name, {})



