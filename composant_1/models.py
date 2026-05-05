from django.db import models

# Create your models here.

class Etudiants(models.Model): 
    nom= models.CharField(max_length=150)
    Prenom  =  models.CharField(max_length=150)
    age= models.IntegerField()
    presentation= models.TextField()
    
    def __str__(self):
     return self.nom

    
    