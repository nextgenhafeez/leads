#!/usr/bin/env python
import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Create a custom admin.py file for User
custom_admin_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'custom_user_admin.py')

# Write the custom admin file
with open(custom_admin_file, 'w') as f:
    f.write("""
from django.contrib import admin
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
""")
    print(f"Created {custom_admin_file}")

# Now update the config/urls.py file to import this custom admin
urls_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config', 'urls.py')
if os.path.exists(urls_file):
    with open(urls_file, 'r') as f:
        urls_content = f.read()
    
    # Add import for our custom admin
    if 'import custom_user_admin' not in urls_content:
        # Find the first import line
        import_index = urls_content.find('import')
        if import_index >= 0:
            # Insert our import after the first import
            new_content = urls_content[:import_index] + 'import custom_user_admin\n' + urls_content[import_index:]
            
            # Write the updated content
            with open(urls_file, 'w') as f:
                f.write(new_content)
                print(f"Updated {urls_file} to import custom_user_admin")
        else:
            print(f"Could not find import statement in {urls_file}")
    else:
        print(f"custom_user_admin already imported in {urls_file}")
else:
    print(f"urls.py not found at {urls_file}")
