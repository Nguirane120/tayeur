from api_fewnu_compta.serializers import *
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from ..models import Profile


class ProfileList(generics.ListCreateAPIView):
    queryset = Profile
    serializer_class = ProfileSerializer

    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        
        images = request.FILES.getlist('images')
        
        if serializer.is_valid():
            profile = serializer.save()
            
            # Associating uploaded images to the created profile
            for image in images:
                Profile.objects.create(images=image)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, format=None):
        items = Profile.objects.all()
        serializer = ProfileSerializer(items, many=True)
        return Response(serializer.data)
        



class ProfileByUser(generics.RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # permission_classes = []

    def get(self, request, id, format=None):
        try:
            item = Profile.objects.filter(userId=id)
            serializer = ProfileSerializer(item,many=True)
            return Response(serializer.data)
        except Profile.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)