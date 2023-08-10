from rest_framework import serializers
from .models import  Horaire



class HoraireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horaire
        fields = '__all__'
