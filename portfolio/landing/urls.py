from django.urls import path
from . import views

urlpatterns = [
    path('es', views.español, name="español"),
    path('en', views.english, name="english")
]

