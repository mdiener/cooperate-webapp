from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from .forms import SignupForm, LoginForm

def signup(request):
  if request.method == "GET":
    return render(request, "user/signup.html", { "form": SignupForm() })
  elif request.method == "POST":
    form = SignupForm(request.POST)

    if form.is_valid():
      email = form.cleaned_data["email"]
      password = form.cleaned_data["password"]

      user = User.objects.create_user(username=email, email=email, password=password)
      group = Group.objects.get(name="ads-viewer")
      user.groups.set([group])
      user.first_name = form.cleaned_data["first_name"]
      user.last_name = form.cleaned_data["last_name"]
      user.save()

      return HttpResponseRedirect("/login")
    else:
      return HttpResponseRedirect("/signup")


def login(request):
  if request.method == "GET":
    if request.user.is_authenticated:
      return HttpResponseRedirect("/ads")

    return render(request, "user/login.html", { "form": LoginForm() })
  elif request.method == "POST":
    form = LoginForm(request.POST)
    if form.is_valid():
      user = authenticate(request, username=form.cleaned_data["email"], password=form.cleaned_data["password"])

      if user is not None:
        django_login(request, user)

        return HttpResponseRedirect("/ads")
      else:
        return HttpResponseRedirect("/signup")
    else:
      return HttpResponseRedirect("/signup")


def logout(request):
  django_logout(request)
  return HttpResponseRedirect("/login")
