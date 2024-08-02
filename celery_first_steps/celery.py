import os

from celery import Celery
from celery.beat import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "celery_first_steps.settings")

app = Celery("celery_first_steps")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

app.conf.beat_schedule = {
    "send-ad-mail-5-minutes": {
        "task": "mail_app.tasks.send_ad_mails",
        "schedule": crontab(minute="*/5"),
        "args": ("Email enviado automaticamente",),
    }
}


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
