from rest_framework import generics
from rest_framework.response import Response

from .models import  Horaire
from .serializers import  HoraireSerializer



class HoraireList(generics.ListCreateAPIView):
    queryset = Horaire.objects.all()
    serializer_class = HoraireSerializer

    def post(self, request, format=None):
        serializer = HoraireSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors, status=400)
        
    def get(self, request, format=None):
        items = Horaire.objects.filter(archived=False).order_by('pk')
        serializer = HoraireSerializer(items, many=True)
        return Response(serializer.data)
    



class HoraireByIdAPIView(generics.RetrieveUpdateDestroyAPIView):
  
    queryset = Horaire.objects.all()
    serializer_class = HoraireSerializer

    def get(self, request, id, format=None):
        try:
            item = Horaire.objects.filter(archived=False).get(pk=id)
            serializer = HoraireSerializer(item)
            return Response(serializer.data)
        except Horaire.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)

    def put(self, request, id, format=None):
        try:
            item = Horaire.objects.filter(archived=False).get(pk=id)
        except Horaire.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)
        self.data = request.data.copy()        
        serializer = HoraireSerializer(item, data= self.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    # def delete(self, request, id, format=None):
    def delete(self, request, *args, **kwargs):
        try:
            item = Horaire.objects.filter(archived=False).get(id=kwargs["id"])
        except Horaire.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)
        item.archived=True
        item.save()
        return Response({"message": "deleted"},status=204)



class HoraireByUser(generics.RetrieveAPIView):
    queryset = Horaire.objects.all()
    serializer_class = HoraireSerializer
        
    def get(self, id, request, format=None):
        items = Horaire.objects.filter(archived=False, createdBy=id)
        serializer = HoraireSerializer(items, many=True)
        return Response(serializer.data)