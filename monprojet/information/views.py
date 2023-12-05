from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .form import *



# Create your views here.

'''class Nouveau(APIView):
    def get(self, request):
        data = {'tse':'fyguygv'}
        return Response(Note.objects.all())'''