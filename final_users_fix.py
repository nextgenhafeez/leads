#!/usr/bin/env python
import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Check if User is registered in the auth app
try:
    admin.site.unregister(User)
    print("Successfully unregistered User from AUTHENTICATION AND AUTHORIZATION")
except admin.sites.NotRegistered:
    print("User was not registered in AUTHENTICATION AND AUTHORIZATION")

# Now let's check if it's registered in the users app
from users.models import User as UsersUser

# Check if the custom User model is registered
try:
    admin.site.register(UsersUser)
    print("Registered custom User model from users app")
except admin.sites.AlreadyRegistered:
    print("Custom User model already registered")

print("User model configuration updated")
