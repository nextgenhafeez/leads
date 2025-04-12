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

# Now let's find the app where the USERS section is defined
from django.apps import apps
users_app = None
for app_config in apps.get_app_configs():
    if hasattr(app_config, 'verbose_name') and app_config.verbose_name == 'USERS':
        users_app = app_config
        break
    # Also check models in this app to see if they're in the USERS section
    for model in app_config.get_models():
        if model.__name__ in ['Activities', 'Agents', 'Companies', 'Files']:
            users_app = app_config
            break
    if users_app:
        break

if users_app:
    print(f"Found USERS app: {users_app.name}")
    # Create a custom admin for the User model
    class UsersModelAdmin(UserAdmin):
        pass
    
    # Register User with our custom admin
    admin.site.register(User, UsersModelAdmin)
    print(f"Registered User in app: {users_app.name}")
else:
    print("Could not find the USERS app")
