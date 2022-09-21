from api_fewnu_compta.serializers import *
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.forms.models import model_to_dict
from django.db.models import Count
import json 
from django.db.models import Sum

# clients 

class DepenseArticleAPIListView(generics.CreateAPIView):
    serializer_class = DepenseArticleSerializer
    queryset = DepenseArticle.objects.all()

    def get(self, request, format=None):
        items = DepenseArticle.objects
        serializer = DepenseArticleSerializer(items, many=True)
        return Response({"count": items.count(),"data":serializer.data})  
    
    def post(self, request, format=None):
        data = request.data
        product_id = data['products']
        product = Product.objects.get(id=product_id)
        qte_achete = data['prod_qte']
        product.qte += qte_achete
        data['total']= qte_achete * product.prix_achat
        serializer = DepenseArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print("serializer data",serializer.data)
            updateProduct = ProductSerializer(product, data= data, partial= True)
            if updateProduct.is_valid():
                updateProduct.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors, status=400)

class DepenseArticleByIdAPIView(generics.CreateAPIView):
    # permission_classes = (
    #     permissions.IsAuthenticated,
    # )
    queryset = DepenseArticle.objects.all()
    serializer_class = DepenseArticleSerializer

    def get(self, request, id, format=None):
        try:
            item = DepenseArticle.objects.get(pk=id)
            serializer = DepenseArticleSerializer(item)
            return Response(serializer.data)
        except DepenseArticle.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)

    def put(self, request, id, format=None):
        try:
            data = request.data
            item = DepenseArticle.objects.get(pk=id)
            article = DepenseArticle.objects.get(id=id)
            new_qte_achete = data['prod_qte']
            qte_achete = abs(new_qte_achete - article.prod_qte)
            if(new_qte_achete> article.prod_qte):
                article.products.qte += qte_achete
                item.total = new_qte_achete * article.products.prix_achat
            else:
                article.products.qte -= qte_achete
                item.total = new_qte_achete * article.products.prix_achat
        except Article.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)    
        print("request data",request.data)
        serializer = DepenseArticleSerializer(item, data=request.data, partial= True)
        if serializer.is_valid():
            article.products.save()
            serializer.save()
            return Response(serializer.data)
        return Response("serializer.errors", status=400)

    def delete(self, request, *args, **kwargs):
        try:
            item = DepenseArticle.objects.get(id=kwargs["id"])
            item.products.qte += item.prod_qte
            item.products.save()
        except DepenseArticle.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)
        item.delete()
        return Response({"message": "deleted"},status=204)