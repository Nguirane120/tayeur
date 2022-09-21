from api_fewnu_compta.serializers import *
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.forms.models import model_to_dict
from django.db.models import Avg, Count, Min, Sum
import json 

# clients 

class DepenseAPIView(generics.CreateAPIView):
    """
    POST api/v1/Depense/
    """
    queryset = Depense.objects.all()
    serializer_class = DepenseSerializer

    def get(self, request, format=None):
        items = Depense.objects.filter(archived=False).order_by('pk')
        serializer = DepenseSerializer(items, many=True)
        return Response({"count": items.count(),"data":serializer.data})  
    
    def post(self, request, format=None):
        # commande = request.data.pop('commande')
        serializer = DepenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors, status=400)

class DepenseByIdAPIView(generics.CreateAPIView):
    # permission_classes = (
    #     permissions.IsAuthenticated,
    # )
    queryset = Depense.objects.all()
    serializer_class = DepenseSerializer

    def get(self, request, id, format=None):
        try:
            item = Depense.objects.filter(archived=False).get(pk=id)
            serializer = DepenseSerializer(item)
            return Response(serializer.data)
        except Depense.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)

    def put(self, request, id, format=None):
        try:
            item = Depense.objects.filter(archived=False).get(pk=id)
        except Depense.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)
        self.data = request.data.copy()        
        serializer = DepenseSerializer(item, data= self.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, *args, **kwargs):
        try:
            item = Depense.objects.filter(archived=False).get(id=kwargs["id"])
        except Depense.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)
        item.archived=True
        item.save()
        return Response({"message": "deleted"},status=204)
