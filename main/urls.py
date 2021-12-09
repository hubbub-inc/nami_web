from django.urls import path
from . import views
from .views import service
from django.views.generic import TemplateView

app_name = 'home'

urlpatterns = [
    path('', views.about, name='home'),
    path('about', views.about),
    path('home/<int:pk>/', views.service.as_view(), name='program_detail'),




    path('services', views.services),
    path('contact', views.contact),
    path('education', views.education),
]
