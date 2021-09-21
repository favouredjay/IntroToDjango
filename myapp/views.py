from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, "home.html")


def create_a_cohort(request):
    return render(request, "create_a_cohort.html")


def create_a_native(request):
    return render(request, "create_a_native.html")


def fetch_a_native(request):
    return render(request, "fetch_a_native.html")
