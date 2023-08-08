from rest_framework import generics, permissions, status
from api_fewnu_compta.serializers import *
from django.contrib.auth import authenticate, login
from rest_framework.response import Response

# list user 
class UserAPIView(generics.CreateAPIView):
    """
    GET api/v1/users/
    POST api/v1/users/
    """
    # queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        user = User.objects.all().order_by('-date_joined')
        if not user:
            return Response({
                "status": "failure",
                "message": "no such item",
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user, many=True)

        return Response({
            "status": "success",
            "message": "user successfully retrieved.",
            "count": user.count(),
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def post(self, request):
        #user = request.data
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UserById(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (
    #     permissions.IsAuthenticated,
    # )
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def put(self, request, id, format=None):
        try:
            item = User.objects.filter(archived=False).get(pk=id)
        except User.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404) 
        serializer = UserSerializer(item, data=request.data, partial= True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class UserUpdatePassword(generics.CreateAPIView):
    # permission_classes = (
    #     permissions.IsAuthenticated,
    # )
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def put(self, request, id, format=None):
        try:
            item = User.objects.filter(archived=False).get(pk=id)
            password = request.data['password']
            item.set_password(password)
            item.save()
        except User.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404) 
        
        # serializer = UserSerializer(item, data=request.data, partial= True)
        # if serializer.is_valid(raise_exception=True):
            # serializer.save()
            # return Response(serializer.data)
        return Response("serializer.errors", status=200)