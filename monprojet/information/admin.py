
from django.contrib import admin
from .models import Apprentis, Note, Employe, Bachelier, Module, Formateur, Inscription

class EmployeInline(admin.TabularInline):
    model = Employe
    extra = 0  # Vous pouvez ajuster le nombre initial de formulaires

class BachelierInline(admin.TabularInline):
    model = Bachelier
    extra = 0

class NoteInline(admin.TabularInline):  # Ou admin.TabularInline
    model = Note
    extra = 1  # Nombre de formulaires d'inline à afficher

@admin.register(Apprentis)
class ApprentisAdmin(admin.ModelAdmin):
    inlines = [NoteInline] 
    list_display = ( 'Nom', 'Prenom', 'DateNaiss', 'Sexe', 'CIN', 'Adresse', 'Tel', 'Email')
    
    def get_inline_instances(self, request, obj=None):
        if obj:  # obj sera None lors de la création d'un nouvel enregistrement
            if hasattr(obj, 'employe'):
                return [EmployeInline(self.model, self.admin_site)]
            elif hasattr(obj, 'bachelier'):
                return [BachelierInline(self.model, self.admin_site)]
        return super().get_inline_instances(request, obj)

@admin.register(Note)    
class NoteAdmin(admin.ModelAdmin):
    list_display = ( 'NotePratique', 'NoteTheorique', 'IdApprentis', 'calcul_note', 'statut_autorisation')

@admin.register(Employe)
class EmployeAdmin(admin.ModelAdmin):
    list_display = ['Nom', 'Prenom', 'DateNaiss', 'Sexe', 'CIN', 'Adresse', 'Tel', 'Email', 'LieuTravail', 'Fonction']

@admin.register(Bachelier)
class BachelierAdmin(admin.ModelAdmin):
    list_display = ['Nom', 'Prenom', 'DateNaiss', 'Sexe', 'CIN', 'Adresse', 'Tel', 'Email', 'DateSession', 'Serie', 'CentreExamen', 'Mention', 'NumInscriBacc']

#class EmployeAdmin(admin.ModelAdmin):
   # list_display = ('Nom', 'Prenom', 'CIN', 'Adresse', 'Tel', 'Email', 'LieuTravail', 'Fonction')

#class BachelierAdmin(admin.ModelAdmin):
 #   list_display = ('Nom', 'Prenom', 'CIN', 'Adresse', 'Tel', 'Email', 'DateSession', 'Serie', 'CentreExamen', 'Mention', 'NumInscriBacc')

class ModuleAdmin(admin.ModelAdmin):
    list_display = ('NomModule', 'Droit')

class FormateurAdmin(admin.ModelAdmin):
    list_display = ( 'NomFormater', 'EmailFormater', 'TelFormater', 'Certification', 'IdModule')

class InscriptionAdmin(admin.ModelAdmin):
    list_display = ( 'DateInscri', 'TotalDroit', 'IdApprentis', 'IdModule')



# Enregistrez les modèles avec leurs classes d'administration respectives
#admin.site.register(Apprentis, ApprentisAdmin)
#admin.site.register(Note, NoteAdmin)
#admin.site.register(Employe, EmployeAdmin)
#admin.site.register(Bachelier, BachelierAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(Formateur, FormateurAdmin)
admin.site.register(Inscription, InscriptionAdmin)


