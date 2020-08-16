from django.views.generic import TemplateView
from django.urls import path

from note import views


app_name = 'note'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add/', views.AddNoteView.as_view(), name='add'),
    path('get/<int:pk>/', views.GetNoteView.as_view(), name='get'),
]
