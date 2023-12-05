'''from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import *
from .models import *
'''
# Dans votre fichier viewsets.py

from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Apprentis, Note, Employe, Bachelier, Module, Formateur, Inscription
from .serializers import ApprentisSerializer, NoteSerializer, EmployeSerializer, BachelierSerializer, ModuleSerializer, FormateurSerializer, InscriptionSerializer

class ApprentisViewSet(viewsets.ModelViewSet):
    queryset = Apprentis.objects.all()
    serializer_class = ApprentisSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class EmployeViewSet(viewsets.ModelViewSet):
    queryset = Employe.objects.all()
    serializer_class = EmployeSerializer

class BachelierViewSet(viewsets.ModelViewSet):
    queryset = Bachelier.objects.all()
    serializer_class = BachelierSerializer

class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

class FormateurViewSet(viewsets.ModelViewSet):
    queryset = Formateur.objects.all()
    serializer_class = FormateurSerializer

class InscriptionViewSet(viewsets.ModelViewSet):
    queryset = Inscription.objects.all()
    serializer_class = InscriptionSerializer


'''
class UserViewSet(viewsets.ModelViewSet) :
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ApprentisViewSet(viewsets.ModelViewSet) :
    queryset = Apprentis.objects.all()
    serializer_class = ApprentisSerializer

class NoteViewSet(viewsets.ModelViewSet) :
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    '''