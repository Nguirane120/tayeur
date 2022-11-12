from api_fewnu_compta.serializers import *
from rest_framework import generics, status
from rest_framework.response import Response
from api_fewnu_compta.models import Paiement
# from rest_framework.generics import UpdateAPIView
from rest_framework.decorators import api_view




class CreationPaiementAPIView(generics.ListCreateAPIView):
    queryset = Paiement.objects.all()
    serializer_class = PaiementSerializer

    def get(self, request, format=None):
        paiement = Paiement.objects.all()
        serializer = PaiementSerializer(paiement, many=True)

        return Response(serializer.data, status=200)

class ModifierPaiementAPIView(generics.UpdateAPIView):
    queryset = Paiement.objects.all()
    serializer_class = PaiementSerializer

    def get(self, request, pk, format=None):
        paiement = Paiement.objects.get(pk=pk)
        serializer = PaiementSerializer(paiement)
        return Response(serializer.data, status=200)

    def put(self, request, pk,format=None):
        paiement = Paiement.objects.get(pk=pk)
        serializer = PaiementSerializer(paiement, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def delete(self, request, *args, **kwargs):
        try:
            paiement = Paiement.objects.filter(archived=False).get(id=kwargs["pk"])
        except Paiement.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)
        paiement.archived=True
        paiement.save()
        return Response({"message": "deleted"},status=204)
 