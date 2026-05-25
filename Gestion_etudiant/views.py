from django.shortcuts import render
from django.views.generic import ListView
from .models import Etudiant

# Create your views here.

def lister_etudiant(request):
    etudiants = Etudiant.objects.all()
    context = {'etudiants': etudiants}
    return render(request, 'etudiant_list.html', context)




def enregistrer_etudiant(request):

    if request.method == 'POST':
        etudiant = Etudiant(
            nom = request.POST['nom'],
            prenom = request.POST['prenom'],
            age = request.POST['age'],
            email = request.POST['email'],
            classe = request.POST['classe'],
            date_inscription = request.POST['date_inscription'],
        )
        etudiant.save()
        
        return redirect('lister_etudiant')
    context = {'etudiant': etudiant}
    return render(request, 'Enregistrement.html', context)  