from mail_app.models import Widget

from celery import shared_task
from django.core.mail import send_mail
from celery_first_steps import settings


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(nums):
    return sum(nums)


@shared_task
def count_widgets():
    return Widget.objects.count()


@shared_task
def rename_widget(widget_id, name):
    w = Widget.objects.get(id=widget_id)
    w.name = name
    w.save


@shared_task(bind=True)
def send_ad_mails(self, message):
    # recipient_list = ["cassiano.schneider@grupovoalle.com.br"]
    recipient_list = ["work.walter.marinho@gmail.com"]
    mail_subject = "Email teste celery"
    send_mail(
        subject=mail_subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=recipient_list,
        fail_silently=False,
    )
    return "Email Sent"
