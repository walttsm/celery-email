serve-django:
	python manage.py runserver

worker-up:
	celery -A celery_first_steps worker --pool=solo -l info

beat-up:
	celery -A celery_first_steps beat -l INFO