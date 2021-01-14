from django.contrib import admin
from .models import APIKey

@admin.register(APIKey)
class APIKeyModelAdmin(admin.ModelAdmin):
    pass