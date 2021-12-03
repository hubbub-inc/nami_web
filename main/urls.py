from django.urls import path
from . import views
from .views import service
from django.views.generic import TemplateView

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about),
    path('home/<pk>/', views.service.as_view()),


    path('services', views.services),
    path('contact', views.contact),
]