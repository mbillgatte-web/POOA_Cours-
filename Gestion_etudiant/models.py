from django.db import models

# Create your models here.

class Etudiant(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    date_inscription = models.DateField(auto_now_add=True)
    classe = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nom} {self.prenom}"
