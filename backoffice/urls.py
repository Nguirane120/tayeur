from django.urls import include, path 

from .views import *

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path('users', usersList, name='users'),
    path('clients', clientsList, name='clients'),
    path('commandes', commandeList, name='commandes'),
    path("login", loginPage, name="login"),
    path("logout", logOutUser, name="logout"),
]   
