from threading import local
from django.shortcuts import render
from simplex.forms import ContactForm

def index(request):
    form = ContactForm(request.GET or None)
    return render(request, 'algoritmo/index.html',locals())
