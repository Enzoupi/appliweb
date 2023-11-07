from django.views.generic import (TemplateView)

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
class AccueilView(TemplateView):
    template_name = 'accueil.html'

