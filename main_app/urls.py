from django.urls import path
from . import views

urlpatterns = [

path('', views.home, name='home'),
path('results/', views.generate, name='generate'),
path('filter_results/', views.filter_results, name='filter_results'),
path('generate_playlist/', views.generate_playlist, name='generate_playlist'),
# path('about/', views.about, name='about'),

]