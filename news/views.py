from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item

def display_news_images(request):
    if request.method == 'GET':

        items = Item.objects.all()
        return render(request, 'news/display_news_items.html', {'items': items})
# Create your views here.
