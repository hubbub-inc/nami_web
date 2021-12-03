from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'news'

urlpatterns = [
    path('', views.display_news_images, name='news'),
]
