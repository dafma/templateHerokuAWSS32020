from django.contrib import admin
from .models import Perfil

# Register your models here.

@admin.register()
class PerfilAdmin(admin.ModelAdmin):
    pass    