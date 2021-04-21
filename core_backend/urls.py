from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='core_backend'),
    path('about/', views.about, name='about'),

]