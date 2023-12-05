'''from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *'''

# Dans votre fichier serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Apprentis, Note, Employe, Bachelier, Module, Formateur, Inscription

class ApprentisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apprentis
        fields = '__all__'

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

class EmployeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employe
        fields = '__all__'

class BachelierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bachelier
        fields = '__all__'

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'

class FormateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formateur
        fields = '__all__'

class InscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscription
        fields = '__all__'


'''
class UserSerializer(serializers.ModelSerializer) :
    class Meta :
        model = User
        fields = ('id', 'username', 'email')

class ApprentisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apprentis
        fields = '__all__'        

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
        '''