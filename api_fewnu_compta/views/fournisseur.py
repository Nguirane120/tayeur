from api_fewnu_compta.serializers import *
from rest_framework import generics, permissions, status
from rest_framework.response import Response
import io, csv, pandas as pd
from django.http import HttpResponse

# clients 

class FournisseurUploadFileView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer
    
    def post(self, request, *args, **kwargs):
        user_id = request.data['user_id']
        user = User.objects.get(pk=user_id)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        csv_file = serializer.validated_data['csv_file']
        reader = pd.read_csv(csv_file, encoding = "utf-8",error_bad_lines=False)
        for _, row in reader.iterrows():
            new_file = Fournisseur(
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

def FournisseurExportFileView(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="fournisseurs.csv"'},
    )

    writer = csv.writer(response)
    row =["firstName","lastName","telephone","adresse","email"]
    writer.writerow(row)
    for fournisseur in Fournisseur.objects.filter(archived=False):

        row =[
            fournisseur.firstName,
            fournisseur.lastName,
            fournisseur.telephone,
            fournisseur.adresse,
            fournisseur.email
        ]
        writer.writerow(row)

    return response

class FournisseurAPIView(generics.CreateAPIView):
    """
    POST api/v1/fournisseur/
    """
    queryset = Fournisseur.objects.all()
    serializer_class = FournisseurSerializer

    def post(self, request, format=None):
        serializer = FournisseurSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors, status=400)

class FournisseurAPIListView(generics.CreateAPIView):
    """
    GET api/v1/clients/
    """
    queryset = Fournisseur.objects.all()
    serializer_class = FournisseurSerializer

    def get(self, request, format=None):
        items = Fournisseur.objects.filter(archived=False).order_by('pk')
        serializer = FournisseurSerializer(items, many=True)
        return Response({"count": items.count(),"data":serializer.data})

class FournisseurByIdAPIView(generics.CreateAPIView):
    # permission_classes = (
    #     permissions.IsAuthenticated,
    # )
    queryset = Fournisseur.objects.all()
    serializer_class = FournisseurSerializer

    def get(self, request, id, format=None):
        try:
            item = Fournisseur.objects.filter(archived=False).get(pk=id)
            serializer = FournisseurSerializer(item)
            return Response(serializer.data)
        except Fournisseur.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)

    def put(self, request, id, format=None):
        try:
            item = Fournisseur.objects.filter(archived=False).get(pk=id)
        except Fournisseur.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)
        self.data = request.data.copy()        
        serializer = FournisseurSerializer(item, data= self.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    # def delete(self, request, id, format=None):
    def delete(self, request, *args, **kwargs):
        try:
            item = Fournisseur.objects.filter(archived=False).get(id=kwargs["id"])
        except Fournisseur.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)
        item.archived=True
        item.save()
        return Response({"message": "deleted"},status=204)
