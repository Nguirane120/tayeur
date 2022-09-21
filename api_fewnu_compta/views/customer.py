from api_fewnu_compta.serializers import *
from rest_framework import generics, permissions, status
from rest_framework.response import Response
import io, csv, pandas as pd
from ..models import Customer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# clients 

class CustomerUploadFileView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer
    def post(self, request, *args, **kwargs):
        user_id = request.data['user_id']
        user = User.objects.get(pk=user_id)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        csv_file = serializer.validated_data['csv_file']
        reader = pd.read_csv(csv_file, encoding = "utf-8",error_bad_lines=False)
        for _, row in reader.iterrows():
            new_file = Customer(
                firstName= row["firstName"],
                lastName= row['lastName'],
                telephone= row["telephone"],
                adresse= row["adresse"],
                email= row["email"],
                user_id = user
                )
            new_file.save()
        return Response({"status": "success"},
                        status.HTTP_201_CREATED)

def CustomerExportFileView(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="clients.csv"'},
    )

    writer = csv.writer(response)
    row =["firstName","lastName","telephone","adresse","email"]
    writer.writerow(row)
    for customer in Customer.objects.filter(archived=False):

        row =[
            customer.firstName,
            customer.lastName,
            customer.telephone,
            customer.adresse,
            customer.email
        ]
        writer.writerow(row)

    return response

class CustomerAPIView(generics.CreateAPIView):
    """
    POST api/v1/client/
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def post(self, request, format=None):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors, status=400)

class CustomerAPIListView(generics.CreateAPIView):
    """
    GET api/v1/clients/
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get(self, request, format=None):
        items = Customer.objects.filter(archived=False).order_by('pk')
        serializer = CustomerSerializer(items, many=True)
        return Response({"count": items.count(),"data":serializer.data})

class CustomerByIdAPIView(generics.CreateAPIView):
    # permission_classes = (
    #     permissions.IsAuthenticated,
    # )
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get(self, request, id, format=None):
        try:
            item = Customer.objects.filter(archived=False).get(pk=id)
            serializer = CustomerSerializer(item)
            return Response(serializer.data)
        except Customer.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)

    def put(self, request, id, format=None):
        try:
            item = Customer.objects.filter(archived=False).get(pk=id)
        except Customer.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)
        self.data = request.data.copy()        
        serializer = CustomerSerializer(item, data= self.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    # def delete(self, request, id, format=None):
    def delete(self, request, *args, **kwargs):
        try:
            item = Customer.objects.filter(archived=False).get(id=kwargs["id"])
        except Customer.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)
        item.archived=True
        item.save()
        return Response({"message": "deleted"},status=204)
