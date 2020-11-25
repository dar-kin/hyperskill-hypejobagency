from django.contrib.auth.views import LoginView


class MyLoginView(LoginView):
    redirect_authenticated_user = False
    template_name = "customized_login.html"
