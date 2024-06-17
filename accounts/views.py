from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def index(request):
    if request.user.is_staff:
        return redirect("/admin")
    return redirect("shop")


def signup(request):
    if request.method == "POST":
        customer_form = SignupForm(request.POST)
        if customer_form.is_valid():
            customer_form.save()
            return redirect("login")
    else:
        customer_form = SignupForm()

    return render(
        request,
        "accounts/signup.html",
        {
            "form": customer_form,
        },
    )


def account_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect("/admin")
            return redirect("shop")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "accounts/login.html")


def account_logout(request):
    logout(request)
    return redirect("login")
