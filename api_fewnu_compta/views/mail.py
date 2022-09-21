from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from api_fewnu_compta.serializers import *
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.core.mail import EmailMultiAlternatives

def send_email(request):
    subject, from_email, to = 'test envoie facture', 'boymahstar@gmail.com', 'mahmoudbarrysn@gmail.com'
    text_content = 'test text content avec le fichier .'
    html_content = '<p>This is an <strong>important</strong> message.</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_file('media/images/login.png')
    msg.send()
    # subject = request.POST.get('subject', '')
    # message = request.POST.get('message', '')
    # from_email = request.POST.get('from_email', '')
    # message =  "test"
    # message.attach('image/png.png')
    # try:
    #     send_mail("subject", message, 'projetbakeli@gmail.com', ['mahmoudbarrysn@gmail.com'],fail_silently=False,)
    #     return HttpResponse('success.')
    # except BadHeaderError:
    #     return HttpResponse('Invalid header found.')