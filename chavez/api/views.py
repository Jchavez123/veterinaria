from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
# Create your views here.
from api.serializers import usuarioSerializer,tipoVSerializer, mascotaSerializer,historiaSerializer,controlvSerializer
from veterinaria.models import usuario,tipoV,mascota,historia,controlv



class usuarioViewSet(viewsets.ModelViewSet):
 """
 API endpoint para Restaurantes
 """
 queryset = usuario.objects.all()
 serializer_class = usuarioSerializer
permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class tipoViewSet(viewsets.ModelViewSet):
    queryset = tipoV.objects.all()
    serializer_class = tipoVSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class mascotaViewSet(viewsets.ModelViewSet):
    queryset = mascota.objects.all()
    serializer_class = mascotaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class historiaViewSet(viewsets.ModelViewSet):
    queryset = historia.objects.all()
    serializer_class = historiaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class controlvViewSet(viewsets.ModelViewSet):
    queryset = controlv.objects.all()
    serializer_class = controlvSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    