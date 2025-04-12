#!/usr/bin/env python3
import os
import shutil
import django
from django.contrib import admin

# Get the path to the admin static files
admin_static_path = os.path.join(os.path.dirname(admin.__file__), 'static', 'admin')

# Create the destination directories
os.makedirs('static/admin/css', exist_ok=True)
os.makedirs('static/admin/img', exist_ok=True)
os.makedirs('static/admin/js', exist_ok=True)

# Copy the CSS files
css_source = os.path.join(admin_static_path, 'css')
css_dest = 'static/admin/css'

for css_file in ['base.css', 'login.css', 'responsive.css']:
    source_file = os.path.join(css_source, css_file)
    dest_file = os.path.join(css_dest, css_file)
    if os.path.exists(source_file):
        shutil.copy2(source_file, dest_file)
        print(f"Copied {css_file}")

# Copy necessary image files
img_source = os.path.join(admin_static_path, 'img')
img_dest = 'static/admin/img'

for img_file in os.listdir(img_source):
    source_file = os.path.join(img_source, img_file)
    dest_file = os.path.join(img_dest, img_file)
    if os.path.isfile(source_file):
        shutil.copy2(source_file, dest_file)
        print(f"Copied {img_file}")

print("Admin static files copied successfully")
