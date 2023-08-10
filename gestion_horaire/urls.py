from django.urls import path
from .views import  HoraireList

urlpatterns = [
    path('horaires/', HoraireList.as_view(), name='horaire-list'),
]
