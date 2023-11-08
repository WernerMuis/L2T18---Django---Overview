from django.shortcuts import render
from django.http import HttpResponse

# Function to return the index page.
def index(request):
    return render(request, "index.html")

# Function to return the Online Shop page.
def shop(request):
    return render(request, "OnlineShop.html")

# Function to return the Contact Us page.
def contact(request):
    return render(request, "contactUs.html")
