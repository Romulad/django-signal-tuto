from django.views import View
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .models import MyUser


@method_decorator(csrf_exempt, name="dispatch")
class CreateUserView(View):

    def get(self, request):
        view = """
                <form method="POST">
                    <label>
                        Username
                        <input type="text" placeholder="username" name="usern"
                        style="margin-bottom:20px; border-radius:10px; display:block;
                        padding:10px">
                        </input>
                    </label>

                    <label>
                        Password
                        <input type="password" placeholder="password" name="passw"
                        style="margin-bottom:20px; border-radius:10px; display:block;
                        padding:10px"></input>
                    </label>

                    <input type="submit" value="Create an user"
                    style="margin-bottom:20px; display:block;
                    padding:5px"></input>
                </form>
            """
        return HttpResponse(view)

    def post(self, request):
        data = request.POST

        try:
            MyUser.objects.get(username=data["usern"])
            return HttpResponse('This username is already taken')
        except MyUser.DoesNotExist:
            MyUser.objects.create_user(
                username=data["usern"],
                password=data["passw"]
            )
            return HttpResponse('Created')