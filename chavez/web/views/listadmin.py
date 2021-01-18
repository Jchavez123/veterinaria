#from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
#from veterinaria.models import usuario

class listView(View):
    '''
    Vista de la pagina Home
    '''
    template_name = 'admin/lista-admin.html'

    def get(self, request):
        return render(request, self.template_name, {})


class listinternadoView(View):
    '''
    Vista de la pagina Home
    '''
    template_name = 'admin/lista-internado.html'

    def get(self, request):
        return render(request, self.template_name, {})



class clienteView(View):
    '''
    Vista de la pagina Home
    '''
    template_name = 'admin/lista-cliente.html'

    def get(self, request):
        return render(request, self.template_name, {})


class MascotaView(View):
    '''
    Vista de la pagina Home
    '''
    template_name = 'admin/lista-mascota.html'

    def get(self, request):
        return render(request, self.template_name, {})

class vacunaView(View):
    '''
    Vista de la pagina Home
    '''
    template_name = 'admin/lista-vacunas.html'

    def get(self, request):
        return render(request, self.template_name, {})