from django.shortcuts import render

from django.shortcuts import render


def Afficher_user(request ):
    return render(request, 'Affiche user.html')
