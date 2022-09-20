from django.shortcuts import render
from django.views.generic import TemplateView #Classe responsável pela renderização das páginas

class HomeView(TemplateView): #Classe da página principal
    template_name = 'main/index.html'
