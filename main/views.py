from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.views import View
from .models import TestModel, Program
from django.views.generic.detail import DetailView
from datetime import date
import datetime
from cal.models import Meeting, Meeting


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
    upcoming = Meeting.objects.filter(start_time__range=(today, addweek))
    print(upcoming)

    print(addweek)
    template = 'home/about.html'
    meetinglist = [{'title': meeting.program.name, 'programid': meeting.program.pk, 'day': str(meeting.start_time.day), 'month': meeting.start_time.strftime("%B")} for meeting in upcoming]
    meetinglist.reverse()
    context['upcoming'] = meetinglist
    print(meetinglist)

    print('done')
    return render(request, template, context)


def contact(request):
    context = {}


    template = 'home/contact.html'
    return render(request, template, context)

def prog_name(request, name):
    program = Program.objects.get(name=name)
    new_path = '/home/' + str(program.pk)
    return redirect(new_path)

class service(DetailView):
    model = Program
    context_object_name = 'pk'

def services(request):
    groups = Program.objects.all()
    context = {}
    context['groups'] = groups
    template = 'home/services.html'
    return render(request, template, context)
