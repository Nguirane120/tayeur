from django.conf import settings
from ..serializers import MessageSerializer
import os
import twilio
import twilio.rest
from twilio.rest import Client

from django.conf import settings
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response

import twilio
import twilio.rest



class SendTwilioMessageView(APIView):
    def post(self, request, *args, **kwargs):
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)

        message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+15005550006',
                     to='+15558675310'
                 )

        

        return Response({"message_id": message.sid})