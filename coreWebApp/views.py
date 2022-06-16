from django.shortcuts import render
from django.http import HttpResponse
from .models import CompanyDetails
# Create your views here.


def home(request):
    company = CompanyDetails()
    company.name = "ECOURSES"
    company.email = "contact@ecourses.com"
    company.phone = "+1 012 345 6789"
    company.address_city = "Plano"
    company.address_state = "TX"
    company.address_street = "123 Street Name"
    company.address_number = "suite 2"
    company.address_zip = "75025"

    return render(request, 'home.html', {'company': company})




