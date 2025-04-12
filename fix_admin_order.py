#!/usr/bin/env python
import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from django.apps import apps

# First, let's see what's currently registered
print("Currently registered models:")
for model, model_admin in admin.site._registry.items():
    print(f"- {model._meta.app_label}.{model.__name__}")

# Create a custom AdminSite to replace the default one
class CustomAdminSite(admin.AdminSite):
    def get_app_list(self, request):
        """
        Return a sorted list of all the installed apps that have been
        registered in this site.
        """
        app_list = super().get_app_list(request)
        
        # Find the app that contains the User model
        for app in app_list:
            # Check if this is the app with the USERS section
            if app.get('name') == 'USERS' or 'user' in app.get('name', '').lower():
                print(f"Found USERS section: {app['name']}")
                
                # Get the models in this app
                models = app['models']
                
                # Find the User model
                user_model = None
                for i, model in enumerate(models):
                    if model['object_name'] == 'User':
                        print(f"Found User model at position {i}")
                        user_model = models.pop(i)
                        break
                
                # If we found the User model, put it at the beginning
                if user_model:
                    models.insert(0, user_model)
                    app['models'] = models
                    print("Moved User model to the top")
        
        return app_list

# Create an instance of the custom admin site
custom_admin_site = CustomAdminSite(name='custom_admin')

# Copy all the registered models from the default admin site to our custom one
for model, admin_class in list(admin.site._registry.items()):
    custom_admin_site.register(model, type(admin_class))

# Replace the default admin site with our custom one
admin.site = custom_admin_site
admin.sites.site = custom_admin_site

print("Replaced default AdminSite with CustomAdminSite")

# Create a file to apply this patch on startup
os.makedirs('config/patches', exist_ok=True)
patch_file = 'config/patches/admin_ordering.py'
patch_content = """
# Monkey patch the AdminSite to customize model ordering
from django.contrib import admin
from django.contrib.admin.sites import AdminSite

# Store the original method
original_get_app_list = AdminSite.get_app_list

def custom_get_app_list(self, request):
    \"\"\"
    Custom get_app_list method that puts the User model at the top of the USERS section
    \"\"\"
    app_list = original_get_app_list(self, request)
    
    # Find the app with the USERS section
    for app in app_list:
        if app.get('name') == 'USERS' or 'user' in app.get('name', '').lower():
            # Get the models in this app
            models = app['models']
            
            # Find the User model
            user_model = None
            for i, model in enumerate(models):
                if model['object_name'] == 'User':
                    user_model = models.pop(i)
                    break
            
            # If we found the User model, put it at the beginning
            if user_model:
                models.insert(0, user_model)
                app['models'] = models
    
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
