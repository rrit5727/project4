from django.urls import path
from . import views

urlpatterns = [

path('', views.home, name='home'),
path('generate/', views.generate, name='generate')
# path('about/', views.about, name='about'),

]