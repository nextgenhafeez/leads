#!/usr/bin/env python
import os

# Path to the users/admin.py file
users_admin_file = 'users/admin.py'

# New content with a custom admin site
new_users_admin_content = """from django.contrib import admin
from django.contrib.admin import AdminSite

# Create a custom AdminSite to control the order
class CustomAdminSite(AdminSite):
    def get_app_list(self, request):
        app_list = super().get_app_list(request)
        for app in app_list:
            if app['app_label'] == 'users':
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
                    
                # Sort the rest alphabetically
                models[1:] = sorted(models[1:], key=lambda x: x['name'])
                
                # Update the app's models
                app['models'] = models
        return app_list

# Create an instance of the custom admin site
custom_admin_site = CustomAdminSite(name='custom_admin')

# Import all models
from .models import (
    User,
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
)

# Register models with the custom admin site
custom_admin_site.register(User)
custom_admin_site.register(Activity)
custom_admin_site.register(Agent)
custom_admin_site.register(Company)
custom_admin_site.register(Files)
custom_admin_site.register(Followups)
custom_admin_site.register(Form)
custom_admin_site.register(Invitation)
custom_admin_site.register(Lead)
custom_admin_site.register(LeadsGroup)
custom_admin_site.register(Messages)
custom_admin_site.register(SourceType)
custom_admin_site.register(Source)

# Also register with the default admin site
admin.site.register(User)
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

# Path to the urls.py file
urls_file = 'config/urls.py'

# Check if files exist
if not os.path.exists(users_admin_file):
    print(f"Error: {users_admin_file} not found")
    exit(1)

if not os.path.exists(urls_file):
    print(f"Error: {urls_file} not found")
    exit(1)

# Write the new content to users/admin.py
with open(users_admin_file, 'w') as f:
    f.write(new_users_admin_content)
    print(f"Updated {users_admin_file} with custom admin site")

# Now let's check the urls.py file to see if we need to update it
with open(urls_file, 'r') as f:
    urls_content = f.read()

# Check if we need to modify the urls.py file
if 'from users.admin import custom_admin_site' not in urls_content:
    # We need to update the urls.py file
    new_urls_content = urls_content.replace(
        'from django.contrib import admin',
        'from django.contrib import admin\nfrom users.admin import custom_admin_site'
    )
    
    # Replace the admin.site.urls with custom_admin_site.urls
    new_urls_content = new_urls_content.replace(
        'path(settings.ADMIN_URL, admin.site.urls),',
        'path(settings.ADMIN_URL, custom_admin_site.urls),'
    )
    
    # Write the new content
    with open(urls_file, 'w') as f:
        f.write(new_urls_content)
        print(f"Updated {urls_file} to use custom admin site")
else:
    print(f"{urls_file} already uses custom admin site")
