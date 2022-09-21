from django.urls import path
from . import views

urlpatterns = [
    path('', views.echo),
    path('createUser', views.createUser)
]
