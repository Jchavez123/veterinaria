from django.views import View
from django.shortcuts import render


class adminView(View):
    '''
    Vista de la pagina Home
    '''
    template_name = 'admin/index.html'

    def get(self, request):
        return render(request, self.template_name, {})