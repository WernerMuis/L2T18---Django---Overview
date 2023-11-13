from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Album, LiveShow


# Function for the album page.
def album_page(request):
    """Render the album page.

    :param request: The HTTP request.
    :type request: HttpRequest
    :return: Rendered HTML response for the album page.
    :rtype: HttpResponse
    """    
    albums = Album.objects.all()
    return render(request, 'album_page.html', {'albums': albums})


# Function for the live show details page.
def live_shows_page(request):
    """Render the live shows page.

    :param request: The HTTP request.
    :type request: HttpRequest
    :return: Rendered HTML response for the live shows page.
    :rtype: HttpResponse
    """    
    live_shows = LiveShow.objects.all()
    return render(request, 'live_shows_page.html', {'live_shows': live_shows})


# Function for the landing page.
def landing_page(request):
    """Render the landing page.

    If the request method is POST, attempt to authenticate the user.
    If authentication is successful, log in the user and redirect to the landing page.

    :param request: The HTTP request.
    :type request: HttpRequest
    :return: Rendered HTML response for the landing page.
    :rtype: HttpResponse
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('landing_page')
    return render(request, 'landing_page.html')


# Function to register.
def register(request):
    """Handle user registration.

    If the request method is POST, validate the registration form.
    If the form is valid, create a new user, log in, and redirect to the landing page.

    :param request: The HTTP request.
    :type request: HttpRequest
    :return: Rendered HTML response for the registration page.
    :rtype: HttpResponse
    """    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('landing_page')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


# Function for the logging out.
def logout_view(request):
    """Log out the user.

    :param request: The HTTP request.
    :type request: HttpRequest
    :return: Redirect to the landing page after logging out.
    :rtype: HttpResponse
    """    
    logout(request)
    return redirect('landing_page')
