from . import views
from django.urls import path

urlpatterns = [
    path('agendamento/', views.agendamento),
]