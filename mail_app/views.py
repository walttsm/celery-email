from mail_app.models import User

from mail_app.tasks import send_email
from django.http import HttpResponse


class UserView:

    def create_user(request):
        user = User.objects.create(username=request.POST["username"])

        send_email.delay_on_commit(user.pk)
        return HttpResponse("User created")
