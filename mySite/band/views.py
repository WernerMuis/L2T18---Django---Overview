from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Album, LiveShow


# Function for the landing page.
#def landing_page(request):
#    return render(request, 'landing_page.html')


# Function for the album page.
def album_page(request):
    albums = Album.objects.all()
    return render(request, 'album_page.html', {'albums': albums})


# Function for the live show details page.
def live_shows_page(request):
    live_shows = LiveShow.objects.all()
    return render(request, 'live_shows_page.html', {'live_shows': live_shows})


# Function for the landing page.
def landing_page(request):
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
    logout(request)
    return redirect('landing_page')
