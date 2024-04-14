from django import forms

class LoginForm(forms.Form):
    """
    Formulaire de connexion.

    Ce formulaire est utilisé pour collecter les informations d'identification de l'utilisateur
    lors de la connexion.

    Attributes:
        username (CharField): Champ de saisie pour le nom d'utilisateur.
        password (CharField): Champ de saisie pour le mot de passe de l'utilisateur, masqué.
    """
    username = forms.CharField(max_length=63, label='Utilisateur')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')

