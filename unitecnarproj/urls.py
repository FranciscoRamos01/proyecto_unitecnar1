from django.urls import path
from mainapp import views

urlpatterns = [
    path('', views.pruebas),          
    path('pruebas/', views.pruebas),
    path('template/', views.template_view),
]
