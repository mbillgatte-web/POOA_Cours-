from django.http import HttpResponse 
from django.shortcuts import render


def Index (request ):
    return  render(request, 'index.html')

def Accueil (request ):
    return  HttpResponse( " <h1> Je veux 10 Millions et je suis sur la page d'accuel </h1> ")

def Connexion (request ):
    return  HttpResponse( " <h1> Je veux 10 Millions et je suis sur la page de connexion </h1> ")
