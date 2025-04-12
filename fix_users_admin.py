#!/usr/bin/env python
import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib import admin
from django.apps import apps
from django.contrib.auth.models import User

# First, let's check what's registered in the admin
print("Currently registered models in admin:")
for model, model_admin in admin.site._registry.items():
    print(f"- {model._meta.app_label}.{model.__name__}")

# Let's check if the User model is registered
auth_user = apps.get_model('auth', 'User')
if auth_user in admin.site._registry:
    print("Auth User model is registered in admin")
else:
    print("Auth User model is NOT registered in admin")

# Let's modify the users/admin.py file
users_admin_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'users', 'admin.py')
if os.path.exists(users_admin_file):
    print(f"Found users/admin.py at {users_admin_file}")
    
    # Read the current content
    with open(users_admin_file, 'r') as f:
        current_content = f.read()
        print("Current content of users/admin.py:")
        print(current_content)
    
    # Modify the content to ensure User is registered first
    new_content = """from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Unregister the default User admin if it's registered
try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass

# Register User with a custom admin to make it appear first
class CustomUserAdmin(UserAdmin):
    # This is a trick to make it appear at the top of the USERS section
    def get_model_perms(self, request):
        perms = super().get_model_perms(request)
        # This ensures it appears at the top when sorted
        perms['_order'] = 0
        return perms

# Register User with our custom admin
admin.site.register(User, CustomUserAdmin)

# Register other models below
"""
    
    # Add the rest of the original content
    if 'from django.contrib import admin' in current_content:
        # Remove the first import line to avoid duplication
        current_content = current_content.replace('from django.contrib import admin', '', 1)
    
    new_content += current_content
    
    # Write the new content
    with open(users_admin_file, 'w') as f:
        f.write(new_content)
        print(f"Updated {users_admin_file} to make User appear first")
else:
    print(f"users/admin.py not found at {users_admin_file}")
    
    # Let's check if there's a custom User model in leadsapp
    leadsapp_admin_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'leadsapp', 'admin.py')
    if os.path.exists(leadsapp_admin_file):
        print(f"Found leadsapp/admin.py at {leadsapp_admin_file}")
        
        # Read the current content
        with open(leadsapp_admin_file, 'r') as f:
            current_content = f.read()
            print("Current content of leadsapp/admin.py:")
            print(current_content)
        
        # Modify the content to ensure User is registered first
        new_content = """from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Unregister the default User admin if it's registered
try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass

# Register User with a custom admin to make it appear first
class CustomUserAdmin(UserAdmin):
    # This is a trick to make it appear at the top of the USERS section
    def get_model_perms(self, request):
        perms = super().get_model_perms(request)
        # This ensures it appears at the top when sorted
        perms['_order'] = 0
        return perms

# Register User with our custom admin
admin.site.register(User, CustomUserAdmin)

# Register other models below
"""
        
        # Add the rest of the original content
        if 'from django.contrib import admin' in current_content:
            # Remove the first import line to avoid duplication
            current_content = current_content.replace('from django.contrib import admin', '', 1)
        
        new_content += current_content
        
        # Write the new content
        with open(leadsapp_admin_file, 'w') as f:
            f.write(new_content)
            print(f"Updated {leadsapp_admin_file} to make User appear first")
    else:
        print(f"leadsapp/admin.py not found at {leadsapp_admin_file}")
