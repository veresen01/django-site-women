from django.apps import AppConfig


class App1Config(AppConfig):
    verbose_name = "Мой сайт"
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app1'
