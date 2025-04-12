#!/usr/bin/env python
import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib import admin
from django.contrib.admin.sites import AdminSite

# Store the original method
original_get_app_list = AdminSite.get_app_list

# Define the desired order
desired_order = [
    'Activity',
    'Agent',
    'Company',
    'Files',
    'Followups',
    'Form',
    'Invitation',
    'Lead',
    'LeadsGroup',
    'Messages',
    'SourceType',
    'Source',
    'User'
]

def custom_get_app_list(self, request):
    """
    Custom get_app_list method that orders models in the USERS section
    according to the desired_order list
    """
    app_list = original_get_app_list(self, request)
    
    # Find the app with the USERS section
    for app in app_list:
        if app.get('name') == 'USERS':
            # Get the models in this app
            models = app['models']
            
            # Create a dictionary to store models by name
            models_dict = {}
            for model in models:
                models_dict[model['object_name']] = model
            
            # Create a new list of models in the desired order
            new_models = []
            for name in desired_order:
                if name in models_dict:
                    new_models.append(models_dict[name])
            
            # Add any models that weren't in the desired_order list
            for model in models:
                if model['object_name'] not in desired_order:
                    new_models.append(model)
            
            # Replace the models list
            app['models'] = new_models
    
    return app_list

# Replace the method
AdminSite.get_app_list = custom_get_app_list

print("Monkey patched AdminSite.get_app_list to order models in USERS section")

# Create a file to apply this patch on startup
os.makedirs('config/patches', exist_ok=True)
patch_file = 'config/patches/admin_ordering.py'
patch_content = """
# Monkey patch the AdminSite to customize model ordering
from django.contrib import admin
from django.contrib.admin.sites import AdminSite

# Store the original method
original_get_app_list = AdminSite.get_app_list

# Define the desired order
desired_order = [
    'Activity',
    'Agent',
    'Company',
    'Files',
    'Followups',
    'Form',
    'Invitation',
    'Lead',
    'LeadsGroup',
    'Messages',
    'SourceType',
    'Source',
    'User'
]

def custom_get_app_list(self, request):
    \"\"\"
    Custom get_app_list method that orders models in the USERS section
    according to the desired_order list
    \"\"\"
    app_list = original_get_app_list(self, request)
    
    # Find the app with the USERS section
    for app in app_list:
        if app.get('name') == 'USERS':
            # Get the models in this app
            models = app['models']
            
            # Create a dictionary to store models by name
            models_dict = {}
            for model in models:
                models_dict[model['object_name']] = model
            
            # Create a new list of models in the desired order
            new_models = []
            for name in desired_order:
                if name in models_dict:
                    new_models.append(models_dict[name])
            
            # Add any models that weren't in the desired_order list
            for model in models:
                if model['object_name'] not in desired_order:
                    new_models.append(model)
            
            # Replace the models list
            app['models'] = new_models
    
    return app_list

# Replace the method
AdminSite.get_app_list = custom_get_app_list
"""

# Write the patch file
with open(patch_file, 'w') as f:
    f.write(patch_content)
    print(f"Created {patch_file} to apply patch on startup")

# Now update the config/__init__.py file to import this patch
init_file = 'config/__init__.py'
if os.path.exists(init_file):
    with open(init_file, 'r') as f:
        init_content = f.read()

    if 'import config.patches.admin_ordering' not in init_content:
        with open(init_file, 'a') as f:
            f.write('\n# Import admin patches to customize admin ordering\nimport config.patches.admin_ordering\n')
            print(f"Updated {init_file} to import admin_ordering")
else:
    with open(init_file, 'w') as f:
        f.write('# Import admin patches to customize admin ordering\nimport config.patches.admin_ordering\n')
        print(f"Created {init_file} with import for admin_ordering")
