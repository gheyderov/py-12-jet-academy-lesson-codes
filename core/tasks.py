import time
from celery import shared_task
from core.models import Subscriber
from product.models import Product
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

@shared_task
def send_email_to_subscribers():
    emails = Subscriber.objects.values_list('email', flat=True)
    products = Product.objects.all()[:3]
    message = render_to_string('email_to_subscribers.html', {
        'products' : products
    })
    mail = EmailMultiAlternatives(
        subject='Latest Products',
        body = message,
        from_email=settings.EMAIL_HOST_USER,
        to = emails
    )
    mail.content_subtype = 'HTML'
    mail.send()



@shared_task
def export_data():
    print('Export start!')
    time.sleep(10)
    print('Export End!')