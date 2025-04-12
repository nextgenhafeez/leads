#!/usr/bin/env python
import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Check if User model is registered
try:
    admin.site.unregister(User)
    print("User model unregistered")
except admin.sites.NotRegistered:
    print("User model was not registered")

# Register User model with UserAdmin
admin.site.register(User, UserAdmin)
print("User model registered with UserAdmin")

print("Admin configuration updated")
