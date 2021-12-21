from django.shortcuts import render
from microhr.models import Work

def home(request):
    works = Work.objects.all()
    context = {"works": works}
    return render(request, "home.html", context)
