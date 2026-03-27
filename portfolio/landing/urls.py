from django.urls import path
from . import views

urlpatterns = [
    path('', views.español, name="español"),
    path('en', views.english, name="ingles")
]