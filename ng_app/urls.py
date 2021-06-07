from django.urls import path
from . import views

urlpatterns=[
    path("", views.start),
    path("process_money", views.processMoney),
    path("restart", views.restart),
    path("setGoals", views.home),
    path("continue", views.home),
    path("startover", views.start)
]