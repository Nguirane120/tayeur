from django.urls import path
from .views import  HoraireList, HoraireByUser

urlpatterns = [
    path('horraires/', HoraireList.as_view(), name='horaire-list'),
    path('horraires/user/<int:id>/', HoraireByUser.as_view(), name='horaire-list-by-user'),
]
