from api_fewnu_compta.serializers import *
from rest_framework import generics, permissions, status
from rest_framework.response import Response
import io, csv, pandas as pd
from django.db.models import Avg, Count, Min, Sum
from ..models import Statistic
from ..models import Depense
from ..models import Vente
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

class StatisticAPIListView(generics.CreateAPIView):
    """
    GET api/v1/statistic/
    """
    # queryset = Statistic.objects.all()
    serializer_class = StatisticSerializer

    def get(self, request, format=None):
        # depenses = Depense.objects.values('products_id.category').annotate(dcount=Count('products.category')).order_by()
        depenses = Depense.objects
        # depenses = Depense.objects.values('products__category').annotate(cnt=Count('products__category'))
        group_by_category = Depense.objects.values('products__category').annotate(total=Sum('products__depensearticle__total'))
        ventes = Vente.objects.all()

        vente_encours = VenteSerializer(ventes.filter(status="ENCOURS"), many=True)
        vente_paye = VenteSerializer(ventes.filter(status="PAYE"), many=True)
        depenseSerializer = DepenseSerializer(depenses, many=True)
        # venteSerializer = VenteSerializer(ventes, many=True)
        # print("depenseSerializer.data",depenseSerializer.data)

        # montant total vente paye 
        montant_total_paye = 0
        for data in vente_paye.data:
            for item in data['list_products']:
                montant_total_paye += item['total']

        # montant total vente en cours 
        montant_total_encours = 0
        for data in vente_encours.data:
            for item in data['list_products']:
                montant_total_encours += item['total']

        # montant total depense 
        montant_total_depense = 0
        for data in depenseSerializer.data:
            for item in data['list_products']:
                montant_total_depense += item['total']

        return Response(
            {
                "count": depenses.count(),
                "data":{
                    "ventes":{
                        "paye":montant_total_paye,
                        "encours":montant_total_encours,
                    # },"depenses":"depenseSerializer.data"}
                    },"depenses":{
                        "by_category":group_by_category,
                        # "by_category":depenseSerializer.data,
                        "montant_total":montant_total_depense
                    }}
                
            })