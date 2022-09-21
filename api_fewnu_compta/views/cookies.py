from rest_framework import generics, permissions, status
from api_fewnu_compta.serializers import *
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from django.contrib.auth import authenticate, login
from rest_framework_jwt.settings import api_settings
from rest_framework.response import Response
from django.contrib.auth import logout
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator

@method_decorator(ensure_csrf_cookie)
class GetCSRFToken(generics.CreateAPIView):

    def get(self, request, format=None):
        return Response({ 'success': 'CSRF cookie set' })