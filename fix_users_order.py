#!/usr/bin/env python
import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib import admin
from django.contrib.auth.models import User as AuthUser
from django.apps import apps

# Get the custom User model from the users app
CustomUser = apps.get_model('users', 'User')

# First, let's check what's registered
print("Currently registered models:")
for model, model_admin in admin.site._registry.items():
    print(f"- {model._meta.app_label}.{model.__name__}")

# Unregister the custom User model if it's registered
if CustomUser in admin.site._registry:
    admin.site.unregister(CustomUser)
    print(f"Unregistered custom User model")

# Create a custom ModelAdmin for User to make it appear first
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name']
    
    # This is a trick to make it appear at the top
    def get_app_label(self):
        return "aaa_users"  # This will sort before other app labels

# Register the custom User model with our custom admin
admin.site.register(CustomUser, CustomUserAdmin)
print("Registered custom User model with CustomUserAdmin")

# Now update the admin.py file to make this change permanent
admin_file = 'users/admin.py'
new_content = """from django.contrib import admin

# Custom admin for User to make it appear first
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name']
    
    # This is a trick to make it appear at the top
    def get_app_label(self):
        return "aaa_users"  # This will sort before other app labels

from .models import (
    Activity,
    Agent,
    Company,
    Files,
    Followups,
    Form,
    Invitation,
    Lead,
    LeadsGroup,
    Messages,
    Source,
    SourceType,
    User,
)

# Register User with custom admin to make it appear first
admin.site.register(User, CustomUserAdmin)

# Register other models
admin.site.register(Activity)
admin.site.register(Agent)
admin.site.register(Company)
admin.site.register(Files)
admin.site.register(Followups)
admin.site.register(Form)
admin.site.register(Invitation)
admin.site.register(Lead)
admin.site.register(LeadsGroup)
admin.site.register(Messages)
admin.site.register(SourceType)
admin.site.register(Source)
"""

# Write the new content to the admin.py file
with open(admin_file, 'w') as f:
    f.write(new_content)
    print(f"Updated {admin_file} with custom admin for User")
