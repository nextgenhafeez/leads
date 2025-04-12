#!/usr/bin/env python
import os

# Path to the admin.py file
admin_file = 'users/admin.py'

# Check if file exists
if not os.path.exists(admin_file):
    print(f"Error: {admin_file} not found")
    exit(1)

# Read current content
with open(admin_file, 'r') as f:
    current_content = f.read()

# Check if User is already registered
if "admin.site.register(User)" in current_content:
    print("User model is already registered in users/admin.py")
else:
    # Add User registration
    with open(admin_file, 'a') as f:
        f.write("\n# Register User model\nadmin.site.register(User)\n")
    print("Added User model registration to users/admin.py")
