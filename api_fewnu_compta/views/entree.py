from api_fewnu_compta.serializers import *
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt



class EntreeAPIView(generics.ListCreateAPIView):
    """
    POST api/v1/entree/
    """
    queryset = Entree.objects.all()
    serializer_class = EntreeSerializer

    def post(self, request, format=None):
        serializer = EntreeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors, status=400)

    def get(self, request, format=None):
        items = Entree.objects.filter(archived=False).all()
        serializer = EntreeSerializer(items, many=True)
        return Response(serializer.data)



class EntreeByIdAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entree.objects.all()
    serializer_class = EntreeSerializer

    def get(self, request, id, format=None):
        try:
            item = Entree.objects.filter(archived=False).get(pk=id)
            serializer = EntreeSerializer(item)
            return Response(serializer.data)
        except Entree.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)

    def put(self, request, id, format=None):
        try:
            item = Entree.objects.filter(archived=False).get(pk=id)
        except Entree.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)
        self.data = request.data.copy()        
        serializer = EntreeSerializer(item, data= self.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    # def delete(self, request, id, format=None):
    def delete(self, request, *args, **kwargs):
        try:
            item = Entree.objects.filter(archived=False).get(id=kwargs["id"])
        except Entree.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)
        item.archived=True
        item.save()
        return Response({"message": "deleted"},status=204)


class EntreeByUser(generics.RetrieveAPIView):
    queryset = Entree.objects.all()
    serializer_class = EntreeSerializer

    def get(self, request, id, format=None):
        try:
            item = Entree.objects.filter(archived=False).filter(createdBy=id)
            serializer = EntreeSerializer(item)
            return Response(serializer.data)
        except Entree.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
            }, status=404)








