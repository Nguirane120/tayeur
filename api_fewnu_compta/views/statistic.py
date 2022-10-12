from api_fewnu_compta.serializers import *
from rest_framework import generics, permissions, status,viewsets
from rest_framework.response import Response
import io, csv, pandas as pd
from django.db.models.functions import Trunc, Cast,TruncDate,TruncMonth,TruncWeek,TruncYear, TruncDay, TruncHour, TruncMinute, TruncSecond
from django.db.models import Avg, Count, Min, Sum, DateTimeField
from ..models import Depense
from rest_framework.views import APIView
from ..models import Vente
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

class StatisticAPIListView(APIView):
    """
    GET api/v1/statistic/
    """
    # queryset = Statistic.objects.all()
    # serializer_class = StatisticSerializer

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
    
class StatisticByDateAPIView(viewsets.ModelViewSet):

    # def get(self, request, id, format=None):
    serializer_class = VenteSerializer
    queryset = Vente.objects.all()
    filter_fields = {'created_at': ['iexact', 'lte', 'gte']}
    http_method_names = ['get', 'post', 'head']

    GROUP_CASTING_MAP = {  # Used for outputing the reset datetime when grouping
        'day': Cast(TruncDate('created_at'), output_field=DateTimeField()),
        'month': Cast(TruncMonth('created_at'), output_field=DateTimeField()),
        'week': Cast(TruncWeek('created_at'), output_field=DateTimeField()),
        'year': Cast(TruncYear('created_at'), output_field=DateTimeField()),
    }

    GROUP_ANNOTATIONS_MAP = {  # Defines the fields used for grouping
        'day': {
            'day': TruncDay('created_at'),
            'month': TruncMonth('created_at'),
            'year': TruncYear('created_at'),
        },
        'week': {
            'week': TruncWeek('created_at')
        },
        'month': {
            'month': TruncMonth('created_at'),
            'year': TruncYear('created_at'),
        },
        'year': {
            'year': TruncYear('created_at'),
        },
    }

    def list(self, request, *args, **kwargs):
        group_by_field = request.GET.get('group_by', None)
        if group_by_field and group_by_field not in self.GROUP_CASTING_MAP.keys():  # validate possible values
            return Response(status=status.HTTP_400_BAD_REQUEST)

        queryset = self.filter_queryset(self.get_queryset())

        if group_by_field:
            queryset = queryset.annotate(**self.GROUP_ANNOTATIONS_MAP[group_by_field]) \
                .values(*self.GROUP_ANNOTATIONS_MAP[group_by_field]) \
                .annotate(rank=Avg('rank'), created_at=self.GROUP_CASTING_MAP[group_by_field]) \
                .values('rank', 'created_at')

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
