from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.views import View
from .models import TestModel
from django.views.generic.detail import DetailView
from datetime import date
import datetime
from cal.models import Event


def home(request):
    context = {}
    template = 'home/home.html'
    return render(request, template, context)


def about(request):
    context = {}
    print("about")
    today = datetime.datetime.today().date()


    addweek = today + datetime.timedelta(days=20)


    print(type(today))
    print(type(addweek))
    upcoming = Event.objects.filter(start_time__range=(today, addweek))
    print(upcoming)

    print(addweek)
    template = 'home/about.html'
    eventlist = [{'title': event.title, 'day': str(event.start_time.day), 'month': event.start_time.strftime("%B")} for event in upcoming]
    eventlist.reverse()
    context['upcoming'] = eventlist
    print(eventlist)

    print('done')
    return render(request, template, context)


def contact(request):
    context = {}


    template = 'home/contact.html'
    return render(request, template, context)

def prog_name(request, name):
    program = TestModel.objects.get(name=name)
    new_path = '/home/' + str(program.pk)
    return redirect(new_path)

class service(DetailView):
    model = TestModel

def services(request):
    groups = TestModel.objects.all()
    context = {}
    context['groups'] = groups
    template = 'home/services.html'
    return render(request, template, context)
