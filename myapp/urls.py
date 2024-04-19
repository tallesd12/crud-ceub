from . import views
from django.urls import path

urlpatterns = [
    path('agendamento/', views.agendamento, name="views.agendamento"),
    path('agendados/', views.agendados, name="views.agendados"),
    path('json/', views.json, name="views.json"),

]