from api_fewnu_compta.serializers import *
from rest_framework import generics, permissions, status
from rest_framework.response import Response

class CompanyAPIView(generics.CreateAPIView):
    """
    POST api/v1/Company/
    """
    # queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def post(self, request, format=None):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors, status=400)


class CompanyByIdAPIView(generics.CreateAPIView):
    # permission_classes = (
    #     permissions.IsAuthenticated,
    # )
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def get(self, request, id, format=None):
        try:
            item = Company.objects.filter(archived=False).get(user_id=id)
            serializer = CompanySerializer(item)
            return Response(serializer.data)
        except Company.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)

    def put(self, request, id, format=None):
        try:
            item = Company.objects.filter(archived=False).get(pk=id)
        except Company.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)
        self.data = request.data.copy()        
        serializer = CompanySerializer(item, data= self.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, *args, **kwargs):
        try:
            item = Company.objects.filter(archived=False).get(id=kwargs["id"])
        except Company.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)
        item.archived=True
        item.save()
        return Response({"message": "deleted"},status=204)
