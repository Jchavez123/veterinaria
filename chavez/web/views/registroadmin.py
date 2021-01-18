#from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
#from veterinaria.models import usuario

class registroView(View):
    '''
    Vista de la pagina Home
    '''
    template_name = 'admin/registro.html'

    def get(self, request):
        return render(request, self.template_name, {})


class registroclienteView(View):
    '''
    Vista de la pagina Home
    '''
    template_name = 'admin/registro-cliente.html'

    def get(self, request):
        return render(request, self.template_name, {})

class registromascotaView(View):
    '''
    Vista de la pagina Home
    '''
    template_name = 'admin/registro-mascota.html'

    def get(self, request):
        return render(request, self.template_name, {})


class registrovacunaView(View):
    '''
    Vista de la pagina Home
    '''
    template_name = 'admin/registro-vacunas.html'

    def get(self, request):
        return render(request, self.template_name, {})

class registrointernadoView(View):
    '''
    Vista de la pagina Home
    '''
    template_name = 'admin/registro-internado.html'

    def get(self, request):
        return render(request, self.template_name, {})

