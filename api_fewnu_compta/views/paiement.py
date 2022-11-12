from api_fewnu_compta.serializers import *
from rest_framework import generics, status
from rest_framework.response import Response
from api_fewnu_compta.models import Paiement
# from rest_framework.generics import UpdateAPIView
from rest_framework.decorators import api_view


@api_view(['POST'])
def CreationPaiementAPIView(request):
#     print(type(request.data["created_by"]))
    paiement = PaiementSerializer(data=request.data)
    
    # validating for already existing data
    if Paiement.objects.filter(**request.data).exists():
        raise serializers.ValidationError('cette donnée existe déjà')

    if paiement.is_valid():
        paiement.save()
        return Response(paiement.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


#MModifier paiement
@api_view(['POST','GET'])
def ModifierPaiementAPIView(request, pk):
    paiement = Paiement.objects.get(pk=pk)
    print("paiement recupere")
    data = PaiementSerializer(instance=paiement, data=request.data)

    if data.is_valid():
        print("donnée valide")
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)



