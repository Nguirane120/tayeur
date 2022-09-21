from api_fewnu_compta.serializers import *
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.forms.models import model_to_dict
from django.db.models import Avg, Count, Min, Sum
import json 

# clients 

class VenteAPIView(generics.CreateAPIView):
    """
    POST api/v1/Vente/
    """
    queryset = Vente.objects.all()
    serializer_class = VenteSerializer

    def get(self, request, format=None):
        items = Vente.objects.filter(archived=False).order_by('pk')
        serializer = VenteSerializer(items, many=True)
        return Response({"count": items.count(),"data":serializer.data})  
    
    def post(self, request, format=None):
        # commande = request.data.pop('commande')
        serializer = VenteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors, status=400)

class VenteByIdAPIView(generics.CreateAPIView):
    # permission_classes = (
    #     permissions.IsAuthenticated,
    # )
    queryset = Vente.objects.all()
    serializer_class = VenteSerializer

    def get(self, request, id, format=None):
        try:
            item = Vente.objects.filter(archived=False).get(pk=id)
            serializer = VenteSerializer(item)
            return Response(serializer.data)
        except Vente.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)

    def put(self, request, id, format=None):
        try:
            item = Vente.objects.filter(archived=False).get(pk=id)
        except Vente.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)
        self.data = request.data.copy()        
        serializer = VenteSerializer(item, data= self.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, *args, **kwargs):
        try:
            item = Vente.objects.filter(archived=False).get(id=kwargs["id"])
        except Vente.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)
        item.archived=True
        item.save()
        return Response({"message": "deleted"},status=204)
