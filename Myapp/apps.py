"""Including App"""
from django.apps import AppConfig

"""Class for app configuration"""
class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Myapp'
