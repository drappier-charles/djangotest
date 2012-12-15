#-*- coding: utf-8 -*-
# Create your views here.

from test_django.models import Sondage, Reponse
from django.shortcuts import render_to_response

def homepage(request):
    list_sondages = Sondage.objects.all()
    if list_sondages.count() == 0:
        list_sondages = 'Pas de contenu'

    return render_to_response('test_django/homepage.html', { 'list_sondages': list_sondages, 'page_title': 'Accueil des sondages' })