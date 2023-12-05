from django.db import models

# Create your models here.
class Apprentis(models.Model) :
    IdApprentis = models.BigAutoField(primary_key=True)
    Nom = models.CharField(max_length=20)
    Prenom = models.CharField(max_length=50)
    DateNaiss = models.DateField()
    Sexe = models.CharField(max_length=10)
    CIN = models.CharField(max_length=50)
    Adresse = models.CharField(max_length=20)
    Tel = models.CharField(max_length=20)
    Email = models.CharField(max_length=50)

class Note(models.Model) :
    Id = models.BigAutoField(primary_key=True)
    NotePratique = models.DecimalField(max_digits=60, decimal_places=2)
    NoteTheorique = models.DecimalField(max_digits=60, decimal_places=2)
    IdApprentis = models.ForeignKey(Apprentis, on_delete=models.CASCADE)

    def calcul_note(self):
        return self.NotePratique + self.NoteTheorique

    def statut_autorisation(self):
        resultat = self.calcul_note()
        if resultat < 10:
            return "Pas autorisé"
        else:
            return "Autorisé"

class Employe(Apprentis):
    LieuTravail = models.CharField(max_length=20)
    Fonction = models.CharField(max_length=20)

class Bachelier(Apprentis):
    DateSession = models.DateField()
    Serie = models.CharField(max_length=3)
    CentreExamen = models.CharField(max_length=20)
    Mention = models.CharField(max_length=20)
    NumInscriBacc = models.IntegerField()

class Module(models.Model):
    IdModule = models.CharField(max_length=10, primary_key=True)
    NomModule = models.CharField(max_length=20)
    Droit = models.DecimalField(max_digits=64, decimal_places=2)    

class Formateur(models.Model):
    IdFormater = models.IntegerField(primary_key=True)
    NomFormater = models.CharField(max_length=20)
    EmailFormater = models.CharField(max_length=50)
    TelFormater = models.CharField(max_length=20)
    Certification = models.TextField()
    IdModule = models.ForeignKey(Module, on_delete=models.CASCADE)

class Inscription(models.Model):
    NumInscri = models.BigAutoField(primary_key=True)
    DateInscri = models.DateField()
    TotalDroit = models.DecimalField(max_digits=64, decimal_places=2)
    IdApprentis = models.ForeignKey(Apprentis, on_delete=models.CASCADE)
    IdModule = models.ForeignKey(Module, on_delete=models.CASCADE)