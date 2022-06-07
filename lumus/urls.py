from django.urls import path
from .views import PostListView
from . import views



urlpatterns = [
    path('', views.Inicio, name='Inicio'),
    path('navegacao/', PostListView.as_view(), name='navegacao'),



]
