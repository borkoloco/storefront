from django.core.cache import cache
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
import requests
import logging


logger = logging.getLogger(__name__)


class HelloView(APIView):
    # @method_decorator(cache_page(5*60))
    def get(self,request):
        try:
            logger.info('Calling httpbin')
            response= requests.get('https://httpbin.org/delay/2')
            logger.info('Received the response')
            data= response.json()
        except requests.ConnectionError:
            logger.critical('hhtpbin is offline')
        return render(request, 'hello.html', {'name':'Borks'})



# @cache_page(5*60)
# def say_hello(request):
#     response= requests.get('https://httpbin.org/delay/2')
#     data= response.json()
#     return render(request, 'hello.html', {'name':data})




# from django.shortcuts import render
# from .tasks import notify_customers

# def say_hello(request):
#     notify_customers.delay('Hello')
#     return render(request, 'hello.html', {'name': 'Bork'})




# # from django.core.mail import send_mail,mail_admins,BadHeaderError
# from django.core.mail import EmailMessage,BadHeaderError
# from django.shortcuts import render
# from templated_mail.mail import BaseEmailMessage


# def say_hello(request):
#     try:
#         message = BaseEmailMessage(
#             template_name='emails/hello.html',
#             context = {'name':'Bork'}
#         )
#         message.send(['john@borkbuy.com'])
#         # message = EmailMessage('subject','message','from@borkbuy.com',['john@borkbuy.com'])
#         # message.attach_file('playground/static/images/polenta.jpg')
#         # message.send()
#         # mail_admins('subject','message',html_message='message')
#         # send_mail('subject','message','info@borkbuy.com',['bob@borkbuy.com'])
#     except BadHeaderError:
#         pass
#     return render(request, 'hello.html', {'name': 'Bork'})
