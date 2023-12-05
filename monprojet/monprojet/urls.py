
from django.contrib import admin
from django.urls import path, include
from information.viewset import *
from rest_framework import routers
#from jazzmin.views import DashboardView, RegisterView  # Importez les vues correctes
#from jazzmin.views import DashboardView, RegisterView

# Créer un routeur DRF
router = routers.DefaultRouter()
router.register(r'apprentis', ApprentisViewSet, basename='apprentis')
router.register(r'note', NoteViewSet, basename='note')
router.register(r'employe', EmployeViewSet, basename='employe')
router.register(r'bachelier', BachelierViewSet, basename='bachelier')
router.register(r'module', ModuleViewSet, basename='module')
router.register(r'formateur', FormateurViewSet, basename='formateur')
router.register(r'inscription', InscriptionViewSet, basename='inscription')

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('jazzmin/', include('jazzmin.urls')),
    #path('dashboard/', DashboardView.as_view(), name='dashboard'),
    #path('register/', RegisterView.as_view(), name='register'),
    # Inclure les URLs de votre application DRF
    path('api/', include(router.urls)),
]





"""
URL configuration for monprojet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""from django.contrib import admin
from django.urls import path
from information.viewset import *
from rest_framework import routers
from django.contrib.auth.models import User
from django.urls import path, include



urlpatterns = [
    path('', admin.site.urls),
    
]
"""