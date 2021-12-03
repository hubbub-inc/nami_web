from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from django.views import View
from .models import TestModel
from django.views.generic.detail import DetailView


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

class service(DetailView):
    model = TestModel

def services(request):
    groups = TestModel.objects.all()
    context = {}
    context['groups'] = groups
    template = 'home/services.html'
    return render(request, template, context)
