from django.shortcuts import render
from django.http import HttpResponse

def page_accueil_view(request):
    return render(request, 'ChercherTrouver/page_accueil.html')