#!/usr/bin/env python
import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

# Get all models from leadsapp
from django.apps import apps
from django.contrib import admin

# Get the leadsapp models
app_models = apps.get_app_config('leadsapp').get_models()

# Create a new admin.py file
with open('leadsapp/admin.py', 'w') as f:
    f.write('from django.contrib import admin\n')
    f.write('from .models import (\n')
    
    # Write import statements
    model_names = [model.__name__ for model in app_models]
    for i, name in enumerate(model_names):
        if i == len(model_names) - 1:
            f.write(f'    {name},\n')
        else:
            f.write(f'    {name},\n')
    
    f.write(')\n\n')
    
    # Register models with try-except to handle already registered models
    for model in app_models:
        model_name = model.__name__
        if model_name != 'EmailAddress':  # Skip EmailAddress model
            f.write(f'try:\n')
            f.write(f'    admin.site.register({model_name})\n')
            f.write(f'except admin.sites.AlreadyRegistered:\n')
            f.write(f'    pass  # Model already registered\n')

print("Admin file updated successfully!")
