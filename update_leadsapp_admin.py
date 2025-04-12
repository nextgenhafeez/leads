#!/usr/bin/env python
import os

# Path to the admin.py file
admin_file = 'leadsapp/admin.py'

# Content to replace the existing User registration
new_content = """# Import the custom admin configuration
from .custom_admin import *

# Ensure Django auth User is unregistered
from django.contrib import admin
from django.contrib.auth.models import User

# Unregister Django auth User if it's registered
try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass
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
    print(f"Updated {admin_file} to unregister Django auth User")
