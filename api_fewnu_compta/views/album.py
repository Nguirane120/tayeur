from api_fewnu_compta.serializers import *
from rest_framework import generics, permissions, status
from rest_framework.response import Response

# clients 

class AlbumAPIView(generics.CreateAPIView):
    """
    POST api/v1/Album/
    """
    # queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def post(self, request, format=None):
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors, status=400)
        
    def get(self, request, format=None):
        items = Album.objects.filter(archived=False).order_by('pk')
        serializer = AlbumSerializer(items, many=True)
        return Response({"count": items.count(),"data":serializer.data})

class AlbumByIdAPIView(generics.CreateAPIView):
    # permission_classes = (
    #     permissions.IsAuthenticated,
    # )
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def get(self, request, id, format=None):
        try:
            item = Album.objects.filter(archived=False).get(pk=id)
            serializer = AlbumSerializer(item)
            return Response(serializer.data)
        except Album.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)

    def put(self, request, id, format=None):
        try:
            item = Album.objects.filter(archived=False).get(pk=id)
        except Album.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)
        self.data = request.data.copy()        
        serializer = AlbumSerializer(item, data= self.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, *args, **kwargs):
        try:
            item = Album.objects.filter(archived=False).get(id=kwargs["id"])
        except Album.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)
        item.archived=True
        item.save()
        return Response({"message": "deleted"},status=204)
    

class AlbumByUser(generics.RetrieveAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    # permission_classes = []

    def get(self, request, id, format=None):
        try:
            item = Album.objects.filter(archived=False).filter(createdBy=id)
            serializer = AlbumSerializer(item,many=True)
            return Response(serializer.data)
        except Album.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)


