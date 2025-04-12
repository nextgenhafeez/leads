#!/usr/bin/env python
import os

# Path to the users/admin.py file
users_admin_file = 'users/admin.py'

# Original content (simplified version)
original_content = """from django.contrib import admin

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

# Register models
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
admin.site.register(User)
"""

# Check if file exists
if not os.path.exists(users_admin_file):
    print(f"Error: {users_admin_file} not found")
    exit(1)

# Write the original content
with open(users_admin_file, 'w') as f:
    f.write(original_content)
    print(f"Reverted {users_admin_file} to original content")

# Also check if we modified urls.py and revert if needed
urls_file = 'config/urls.py'
if os.path.exists(urls_file):
    with open(urls_file, 'r') as f:
        urls_content = f.read()
    
    if 'from users.admin import custom_admin_site' in urls_content:
        # Revert the changes
        urls_content = urls_content.replace(
            'from django.contrib import admin\nfrom users.admin import custom_admin_site',
            'from django.contrib import admin'
        )
        
        urls_content = urls_content.replace(
            'path(settings.ADMIN_URL, custom_admin_site.urls),',
            'path(settings.ADMIN_URL, admin.site.urls),'
        )
        
        with open(urls_file, 'w') as f:
            f.write(urls_content)
            print(f"Reverted {urls_file} to original content")
