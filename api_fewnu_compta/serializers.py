from api_fewnu_compta import models
from api_fewnu_compta.models import User
from api_fewnu_compta.models import Customer
from api_fewnu_compta.models import Commande
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *
# User = get_user_model()

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= User
        fields = ('phone','lastName','firstName','password','email', 'user_type','adresse')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # return User.objects.create(**validated_data)
        user = User(
            phone=validated_data['phone'],
            firstName=validated_data['firstName'],
            lastName=validated_data['lastName'],
            email=validated_data['email'],
            adresse = validated_data['adresse']
        )
        user.user_type='owner'
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('phone', 'password')

class TokenSerializer(serializers.Serializer):
    """
    This serializer serializes the token data
    """
    token = serializers.CharField(max_length=255)

# for upload file 
class FileUploadSerializer(serializers.Serializer):
    csv_file = serializers.FileField()


# client 
class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, source="createdBy")
    class Meta:
        model = Customer
        fields = ('id', 'nom_complet', 'telephone', 'adresse', 'pays', 'Ville', 'sexe', 'cou', 'epaule', 'longueur_boubou', 'longueur_manche', 'cuisse', 'longueur_pantalon', 'hanche', 'ceinture', 'tour_bras', 'poitrine', 'taille', 'longueur_robe', 'longueur_poitrine', 'bretelle', 'longueur_jupe', 'longueur_haut', 'blouse', 'autre', 'createdBy', 'user','created_at', 'archived')        

# fournisseur 
class FournisseurSerializer(serializers.ModelSerializer):
    # user_id = UserSerializer(read_only=True)
    class Meta:
        model = Fournisseur
        fields =('id','firstName','lastName','telephone','adresse','email','user_id')

# category 
class CategorySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user')
    class Meta:
        model = Category
        fields =('id','category_name','description','user_id','user')

class ProductSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user')
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category')
    class Meta:
        model = Product
        fields =('id','libelle','min_stock','qte','prix_achat','prix_vente','image','category_id','user_id','user','category')
        depth = 1

class ArticleSerializer(serializers.ModelSerializer):
    prod_info = ProductSerializer(source="products",read_only=True)
    class Meta:
        model = Article
        fields = ('id','vente','prod_info','products','prod_qte','total')
        # depth = 1

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields ='__all__'
        # depth = 1
        


class VenteSerializer(serializers.ModelSerializer):
    user_info = UserSerializer(source="user",read_only=True)
    client_info = CustomerSerializer(source="client",read_only=True)
    list_products = ArticleSerializer(source='articles', many=True,read_only=True)
    class Meta:
        model = Vente
        fields =('id','user','facture','user_info','client','client_info','list_products','date','status')
        # depth = 1

class DepenseArticleSerializer(serializers.ModelSerializer):
    prod_info = ProductSerializer(source="products",read_only=True)
    class Meta:
        model = DepenseArticle
        fields = ('id','depense','products','prod_info','prod_qte','total')

# depenses 
class DepenseSerializer(serializers.ModelSerializer):
    user_info = UserSerializer(source="user",read_only=True)
    fournisseur_info = CustomerSerializer(source="fournisseur",read_only=True)
    list_products = DepenseArticleSerializer(source='depense_aticle', many=True,read_only=True)
    class Meta:
        model = Depense
        fields =('id','image','matricule','status','user','user_info','fournisseur','fournisseur_info','list_products','date')
        # depth = 1

# paiement
class PaiementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paiement
        fields = '__all__'
        

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'


class CommandeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, source='createdBy')
    class Meta:
        model = Commande
        fields = ('nom_tissu', 'metre_tissu', 'modele', 'date_livraison', 'montant', 'statut', 'date_commande','clientId', 'createdBy','user' )