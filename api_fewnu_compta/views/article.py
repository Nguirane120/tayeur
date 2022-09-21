from api_fewnu_compta.serializers import *
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.forms.models import model_to_dict
from django.db.models import Count
import json 
from django.db.models import Sum

# clients 

class ArticleAPIListView(generics.CreateAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    def get(self, request, format=None):
        items = Article.objects
        serializer = ArticleSerializer(items, many=True)
        return Response({"count": items.count(),"data":serializer.data})  
    
    def post(self, request, format=None):
        data = request.data
        product_id = data['products']
        product = Product.objects.get(id=product_id)
        qte_vendu = data['prod_qte']
        product.qte -= qte_vendu
        data['total']= qte_vendu * product.prix_vente
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print("serializer data",serializer.data)
            updateProduct = ProductSerializer(product, data= data, partial= True)
            if updateProduct.is_valid():
                updateProduct.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors, status=400)

class ArticleByIdAPIView(generics.CreateAPIView):
    # permission_classes = (
    #     permissions.IsAuthenticated,
    # )
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request, id, format=None):
        try:
            item = Article.objects.get(pk=id)
            serializer = ArticleSerializer(item)
            return Response(serializer.data)
        except Article.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)

    def put(self, request, id, format=None):
        try:
            item = Article.objects.get(pk=id)
            data = request.data
            article = Article.objects.get(id=id)
            new_qte_vendu = data['prod_qte']
            qte_vendu = abs(new_qte_vendu - article.prod_qte)
            if(new_qte_vendu> article.prod_qte):
                article.products.qte -= qte_vendu
                item.total = new_qte_vendu * article.products.prix_vente
            else:
                article.products.qte += qte_vendu
                item.total = new_qte_vendu * article.products.prix_vente 
        except Article.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)
        self.data = request.data.copy()        
        serializer = ArticleSerializer(item, data= self.data, partial= True)
        if serializer.is_valid():
            article.products.save()
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, *args, **kwargs):
        try:
            item = Article.objects.get(id=kwargs["id"])
            item = Article.objects.get(id=kwargs["id"])
            item.products.qte += item.prod_qte
            item.products.save()
        except Article.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)
        item.delete()
        return Response({"message": "deleted"},status=204)