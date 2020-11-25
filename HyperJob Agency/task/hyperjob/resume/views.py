from django.shortcuts import render, redirect
from django.views import View
from resume.models import Resume
from django.http import HttpResponseForbidden
from django import forms


class ResumeListView(View):

    def get(self, request, *args, **kwargs):
        resume = Resume.objects.all()
        return render(request, "resume/resumes.html", context={"resumes": resume})


class DescriptionForm(forms.Form):
        description = forms.CharField(max_length=1024)


class CreateResumeView(View):
    def get(self, request, *args, **kwargs):
        form = DescriptionForm()
        return render(request, "resume/createresume.html", context={"form": form})

    def post(self, request, *args, **kwargs):
        form = DescriptionForm(request.POST)
        description = ""
        if form.is_valid():
            description = form.cleaned_data["description"]
        user = request.user
        if user.is_authenticated and not user.is_staff:
            resume = Resume(description=description, author=user)
            with open("file.txt", "w") as f:
                f.write(str(user.username)+str(description))
            resume.save()
            return redirect("/home")
        else:
            return HttpResponseForbidden('<h1>403 Forbidden</h1>', content_type='text/html')
