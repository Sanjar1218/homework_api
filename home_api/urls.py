from django.urls import path
from . import views

urlpatterns = [
    path('', views.echo),
    path('homework', views.homework),
    path('createUser', views.createUser),
    path('check', views.davomat)
]
