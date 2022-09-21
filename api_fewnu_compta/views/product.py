from api_fewnu_compta.serializers import *
from rest_framework import generics, permissions, status
from rest_framework.response import Response

# clients 

class ProductAPIView(generics.CreateAPIView):
    """
    POST api/v1/Product/
    """
    # queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data,status=201)
        return Response(serializer.errors, status=400)
        
    def get(self, request, format=None):
        items = Product.objects.filter(archived=False).order_by('pk')
        serializer = ProductSerializer(items, many=True)
        return Response({"count": items.count(),"data":serializer.data})

class ProductByIdAPIView(generics.CreateAPIView):
    # permission_classes = (
    #     permissions.IsAuthenticated,
    # )
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, id, format=None):
        try:
            item = Product.objects.filter(archived=False).get(pk=id)
            serializer = ProductSerializer(item)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)

    def put(self, request, id, format=None):
        try:
            item = Product.objects.filter(archived=False).get(pk=id)
        except Product.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)
        self.data = request.data.copy()        
        serializer = ProductSerializer(item, data= self.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, *args, **kwargs):
        try:
            item = Product.objects.filter(archived=False).get(id=kwargs["id"])
        except Product.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)
        item.archived=True
        item.save()
        return Response({"message": "deleted"},status=204)
