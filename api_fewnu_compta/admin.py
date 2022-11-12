from django.contrib import admin
from api_fewnu_compta.models import *
from .models import User
from .models import Customer
from .models import Fournisseur
from .models import Category
from .models import Product
from .models import Depense
from .models import Article
from .models import DepenseArticle
from .models import Company
from .models import Employee

class UserAdmin(admin.ModelAdmin):
    pass

class CustomerAdmin(admin.ModelAdmin):
    pass

class FournisseurAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

class ProductAdmin(admin.ModelAdmin):
    pass

class VenteAdmin(admin.ModelAdmin):
    pass

class DepenseAdmin(admin.ModelAdmin):
    pass

class ArticleAdmin(admin.ModelAdmin):
    pass

class DepenseArticleAdmin(admin.ModelAdmin):
    pass

class CompanyAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Fournisseur, FournisseurAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Vente, VenteAdmin)
admin.site.register(Depense, DepenseAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(DepenseArticle, DepenseArticleAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee)