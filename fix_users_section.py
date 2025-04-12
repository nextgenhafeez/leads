#!/usr/bin/env python
import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# First, unregister User from the default location
try:
    admin.site.unregister(User)
    print("Successfully unregistered User from AUTHENTICATION AND AUTHORIZATION")
except admin.sites.NotRegistered:
    print("User was not registered in AUTHENTICATION AND AUTHORIZATION")

# Create a custom ModelAdmin that changes the app_label
class CustomUserAdmin(UserAdmin):
    def get_model_perms(self, request):
        # This moves the model to a different section in the admin
        perms = super().get_model_perms(request)
        if perms:
            # This is what determines the section in admin
            User._meta.app_label = 'leadsapp'
        return perms

# Register User with our custom admin
admin.site.register(User, CustomUserAdmin)
print("Registered User with custom admin that changes app_label")
