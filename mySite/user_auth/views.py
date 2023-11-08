from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm


def user_login(request):
    """
    Renders a view for the user login page.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTML page for user login.
    """
    return render(request, 'registration/login.html')


def authenticate_user(request):
    """
    Authenticates a user's login credentials and logs them in if valid.

    Args:
        request: The HTTP request object.

    Returns:
        An HTTP redirect to the user's profile page on successful login, or to the login page if authentication fails.
    """
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(
            reverse('user_auth:login')
        )
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('user_auth:show_user')
        )


def show_user(request):
    """
    Renders a view to display the user's username and password.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTML page displaying the user's username and password.
    """
    print(request.user.username)
    return render(request, 'registration/user.html', {
        "username": request.user.username,
        "password": request.user.password
    })


def registration(request):
    """
    Handles user registration by rendering the registration form and processing form submissions.

    Args:
        request: The HTTP request object.

    Returns:
        An HTTP redirect to the login page after successful user registration.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user_auth:login'))
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'registration/registration.html', context)
