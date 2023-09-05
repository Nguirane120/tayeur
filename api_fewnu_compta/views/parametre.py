from api_fewnu_compta.serializers import *
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from ..models import Parametre
from rest_framework.parsers import MultiPartParser, FormParser


class ParametreList(generics.ListCreateAPIView):
    queryset = Parametre
    serializer_class = ParametreSerializer

    # parser_classes = (MultiPartParser, FormParser)

    def post(self, request, format=None):
        serializer = ParametreSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, format=None):
        items = Parametre.objects.all()
        serializer = ParametreSerializer(items, many=True)
        return Response(serializer.data)
        



class ParametreByUser(generics.RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # permission_classes = []

    def get(self, request, id, format=None):
        try:
            item = Parametre.objects.filter(userId=id)
            serializer = ParametreSerializer(item,many=True)
            return Response(serializer.data)
        except Parametre.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)