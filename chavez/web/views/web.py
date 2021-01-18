#from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
#from veterinaria.models import usuario

class hometView(View):
    '''
    Vista de la pagina Home
    '''
    template_name = 'veterinaria/home.html'

    def get(self, request):
        return render(request, self.template_name, {})
