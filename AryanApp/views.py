from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Collobrate

# Create your views here.

def home(request):
    return render(request,"home.html")

def collobrate(request):
    collo_model = Collobrate()
    if request.method == "POST":
        collo_model.fullname = request.POST['fullname']
        collo_model.definition = request.POST['project']
        collo_model.company_name = request.POST['company']
        collo_model.email_address = request.POST['email']
        collo_model.save()
        return render(request,"collobrate.html",{"msg":"Details Submitted! Soon you will get mail"})
    return render(request,"collobrate.html")