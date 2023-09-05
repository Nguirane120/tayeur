from api_fewnu_compta.serializers import *
from rest_framework import generics, permissions, status
from rest_framework.response import Response
import io, csv, pandas as pd
from ..models import Commande
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt



class TransactionAPIView(generics.ListCreateAPIView):
    """
    POST api/v1/commandes/
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def post(self, request, format=None):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors, status=400)

    def get(self, request, format=None):
        items = Transaction.objects.filter(archived=False).all()
        serializer = TransactionSerializer(items, many=True)
        # total_amount = Commande.total_amount()
        # print(total_amount)
        return Response(serializer.data)



class TransactionByIdAPIView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (
    #     permissions.IsAuthenticated,
    # )
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get(self, request, id, format=None):
        try:
            item = Transaction.objects.filter(archived=False).get(pk=id)
            serializer = TransactionSerializer(item)
            return Response(serializer.data)
        except Transaction.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)

    def put(self, request, id, format=None):
        try:
            item = Transaction.objects.filter(archived=False).get(pk=id)
        except Transaction.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)
        self.data = request.data.copy()        
        serializer = TransactionSerializer(item, data= self.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    # def delete(self, request, id, format=None):
    def delete(self, request, *args, **kwargs):
        try:
            item = Transaction.objects.filter(archived=False).get(id=kwargs["id"])
        except Transaction.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)
        item.archived=True
        item.save()
        return Response({"message": "deleted"},status=204)
    


class TransactionByUser(generics.RetrieveAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    def get(self, request, id, format=None):
        try:
            item = Transaction.objects.filter(archived=False).get(pk=id)
            serializer = TransactionSerializer(item)
            return Response(serializer.data)
        except Transaction.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)





