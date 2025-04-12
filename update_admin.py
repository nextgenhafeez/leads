#!/usr/bin/env python
import os

# Path to the admin.py file
admin_file = 'leadsapp/admin.py'

# Content to replace the existing User registration
new_content = """# Import the custom admin configuration
from .custom_admin import *

# Custom User admin that changes the app_label
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# First, unregister User if it's registered
try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass

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
"""

# Check if file exists
if not os.path.exists(admin_file):
    print(f"Error: {admin_file} not found")
    exit(1)

# Read current content
with open(admin_file, 'r') as f:
    current_content = f.read()

# Replace the content
with open(admin_file, 'w') as f:
    f.write(new_content)
    print(f"Updated {admin_file} with new User admin registration")
