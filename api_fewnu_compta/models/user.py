from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone


OWNER = 'owner'
MANAGER = 'manager'
COLLABORATOR = 'collaborator'
TAILLEUR = 'tailleur'

USER_TYPES = (
    (OWNER, OWNER),
    (MANAGER, MANAGER),  
    (COLLABORATOR, COLLABORATOR),    
    (TAILLEUR, TAILLEUR),    
)

class MyUserManager(BaseUserManager):
    def create_user(self, email,lastName,firstName,phone,adresse, password=None):
        """
        Creates and saves a User with the given email, \and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            lastName= lastName,
            firstName = firstName,
            phone= phone,
            adresse= adresse
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,lastName,firstName,phone,adresse, password=None):
        """
        Creates and saves a superuser with the given email, and password.
        """
        user = self.create_user(
            email,
            phone=phone,
            password=password,
            firstName=firstName,
            lastName=lastName,
            adresse=adresse
        )
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser,PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    """
    phone = models.CharField(max_length=40)
    # nom_complet = models.CharField(max_length=100, blank=True)
    firstName = models.CharField(max_length=100, blank=True)
    lastName = models.CharField(max_length=100, blank=True)
    email = models.EmailField(("Email"), max_length=254,unique=True)
    adresse = models.CharField(blank=True, max_length=255, null=True)
    # nom_gerant=models.CharField(max_length=100, blank=True, default="", null=False)
    # nom_boutique=models.CharField(max_length=300, blank=True, null=True)
    # owner_boutique=models.IntegerField(null=True, default=0)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    tailleur = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    user_type = models.CharField(max_length=20, choices=USER_TYPES, blank=True, default=OWNER)
    archived = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['phone','firstName','lastName','adresse']

    # class Meta:
    #     """
    #     For models split into separate files, specify table name and app name.
    #     See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
    #     """
    #     db_table = "api_fewnu_compta_user"
    #     app_label = "api_fewnu_compta"

    def __str__(self):
        return self.email