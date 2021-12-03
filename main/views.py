from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from django.views import View
from .models import TestModel

def home(request):
    context = {}
    template = 'home/home.html'
    return render(request, template, context)


def about(request):
    context = {}
    template = 'home/about.html'
    return render(request, template, context)


def contact(request):
    context = {}
    template = 'home/contact.html'
    return render(request, template, context)


def services(request):
    groups = TestModel.objects.all()
    context = {}
    context['groups'] = groups
    template = 'home/services.html'
    return render(request, template, context)
