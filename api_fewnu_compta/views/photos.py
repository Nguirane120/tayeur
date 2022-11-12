from api_fewnu_compta.serializers import *
from rest_framework import generics, permissions, status
from rest_framework.response import Response

# clients 

class PhotoAPIView(generics.CreateAPIView):
    """
    POST api/v1/Photo/
    """
    # queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def post(self, request, format=None):
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors, status=400)
        
    def get(self, request, format=None):
        items = Photo.objects.filter(archived=False).order_by('pk')
        serializer = PhotoSerializer(items, many=True)
        return Response({"count": items.count(),"data":serializer.data})

class PhotoByIdAPIView(generics.CreateAPIView):
    # permission_classes = (
    #     permissions.IsAuthenticated,
    # )
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def get(self, request, id, format=None):
        try:
            item = Photo.objects.filter(archived=False).get(pk=id)
            serializer = PhotoSerializer(item)
            return Response(serializer.data)
        except Photo.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)

    def put(self, request, id, format=None):
        try:
            item = Photo.objects.filter(archived=False).get(pk=id)
        except Photo.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)
        self.data = request.data.copy()        
        serializer = PhotoSerializer(item, data= self.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, *args, **kwargs):
        try:
            item = Photo.objects.filter(archived=False).get(id=kwargs["id"])
        except Photo.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)
        item.archived=True
        item.save()
        return Response({"message": "deleted"},status=204)

class getListPhotosByAlbumId(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def get(self, request, id, format=None):
        photo = Photo.objects.filter(album=id).all()
        serializer = PhotoSerializer(photo, many=True)
        return Response(serializer.data, status=200)
