from django.views.generic import TemplateView
from django.urls import path

from note import views


app_name = 'note'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
