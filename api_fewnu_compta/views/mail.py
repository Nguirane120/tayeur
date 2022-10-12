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
    msg.attach_file('media/facture/login.png')
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

# class SendMailView(APIView):

#     def post(self, request,client, file):

#         print("request data ",request.data)
        
#         # serializer = self.get_serializer(data=request.data)
#         # serializer.is_valid(raise_exception=True)
#         # csv_file = serializer.validated_data['csv_file']
#         # reader = pd.read_csv(csv_file, encoding = "utf-8",error_bad_lines=False)
#         # for _, row in reader.iterrows():
#         #     new_file = Customer(
#         #         firstName= row["firstName"],
#         #         lastName= row['lastName'],
#         #         telephone= row["telephone"],
#         #         adresse= row["adresse"],
#         #         email= row["email"],
#         #         user_id = user
#         #         )
#         #     new_file.save()

#         return Response({"status": "success"},
#                         status.HTTP_201_CREATED)