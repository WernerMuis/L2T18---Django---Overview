from django.shortcuts import render
from django.http import HttpResponse

# Function to return the index page.
def index(request):
    """Render the index page.

    :param request: The HTTP request.
    :type request: HttpRequest
    :return: Rendered HTML response for the index page.
    :rtype: HttpResponse
    """    
    return render(request, "index.html")

# Function to return the Online Shop page.
def shop(request):
    """Render the Online Shop page.

    :param request: The HTTP request.
    :type request: HttpRequest
    :return: Rendered HTML response for the Online Shop page.
    :rtype: HttpResponse
    """    
    return render(request, "OnlineShop.html")

# Function to return the Contact Us page.
def contact(request):
    """Render the Contact Us page.

    :param request: The HTTP request.
    :type request: HttpRequest
    :return: Rendered HTML response for the Contact Us page.
    :rtype: HttpResponse
    """    
    return render(request, "contactUs.html")
