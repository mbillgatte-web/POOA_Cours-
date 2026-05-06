from django.shortcuts import render
from django.views.generic import ListView
from .models import Etudiant

# Create your views here.

def lister_etudiant(request):
    etudiants = Etudiant.objects.all()
    context = {'etudiants': etudiants}
    return render(request, 'etudiant_list.html', context)