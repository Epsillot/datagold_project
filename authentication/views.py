from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from . import forms


def custom_page_not_found(request, exception):
    """
    Renvoie une page d'erreur 404 personnalisée.

    Args:
        request: L'objet HttpRequest.
        exception: L'exception qui a déclenché l'erreur.

    Returns:
        Un objet HttpResponse avec le contenu de la page d'erreur 404.
    """
    return render(request, '404.html', status=404)


def custom_server_error(request):
    """
    Renvoie une page d'erreur 500 personnalisée.

    Args:
        request: L'objet HttpRequest.

    Returns:
        Un objet HttpResponse avec le contenu de la page d'erreur 500.
    """
    return render(request, '500.html', status=500)


def login_page(request):
    """
    Affiche et gère la page de connexion.

    Args:
        request: L'objet HttpRequest.

    Returns:
        Un objet HttpResponse avec le contenu de la page de connexion.
    """
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('index')
        message = 'Identifiants invalides.'
    return render(request, 'authentication/login.html', context={'form': form, 'message': message})


def logout_user(request):
    """
    Déconnecte l'utilisateur et redirige vers la page de connexion.

    Args:
        request: L'objet HttpRequest.

    Returns:
        Un objet HttpResponseRedirect redirigeant vers la page de connexion.
    """
    logout(request)
    user = request.user  # Récupérer l'utilisateur après la déconnexion
    if not user.is_authenticated:
        print("L'utilisateur a été correctement déconnecté.")
    else:
        print("L'utilisateur n'a pas été correctement déconnecté.")
    return redirect('login')
