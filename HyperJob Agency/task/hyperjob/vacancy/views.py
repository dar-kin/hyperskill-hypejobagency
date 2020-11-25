from django.shortcuts import render, redirect
from django.views import View
from vacancy.models import Vacancy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseForbidden
from django import forms
from django.core.exceptions import PermissionDenied



class MenuView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "vacancy/menu.html", context={})


class VacancyListView(View):

    def get(self, request, *args, **kwargs):
        vacancy = Vacancy.objects.all()
        return render(request, "vacancy/vacancies.html", context={"vacancies": vacancy})


class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = '/login'
    template_name = 'vacancy/signup.html'


class MyLoginView(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = False
    template_name = 'vacancy/login.html'


class UsersView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff:
                return redirect("/vacancy/new")
            else:
                return redirect("/resume/new")
        else:
            raise PermissionDenied


class DescriptionForm(forms.Form):
        description = forms.CharField(max_length=1024)


class CreateVacancyView(View):
    def get(self, request, *args, **kwargs):
        form = DescriptionForm()
        return render(request, "vacancy/createvacancy.html", context={"form": form})

    def post(self, request, *args, **kwargs):
        form = DescriptionForm(request.POST)
        description = ""
        if form.is_valid():
            description = form.cleaned_data["description"]
        user = request.user
        if user.is_authenticated and user.is_staff:
            vacancy = Vacancy(description=description, author=user)
            vacancy.save()
            return redirect("/home")
        else:
            return HttpResponseForbidden('<h1>403 Forbidden</h1>', content_type='text/html')


