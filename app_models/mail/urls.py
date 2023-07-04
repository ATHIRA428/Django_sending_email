from django.urls import path
from .views import send_email_to_user, email_sent

urlpatterns = [

    path('send_email', send_email_to_user, name='send_email'),
    path('email-sent/', email_sent, name='email_sent'),
]
