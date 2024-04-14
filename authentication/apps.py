from django.apps import AppConfig

class AuthenticationConfig(AppConfig):
    """
    Configuration de l'application d'authentification.

    Cette classe de configuration est utilisée pour spécifier la configuration
    spécifique de l'application d'authentification dans Django.

    Attributes:
        default_auto_field (str): Le type de champ automatique par défaut utilisé pour les nouveaux modèles.
        name (str): Le nom de l'application.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authentication'

