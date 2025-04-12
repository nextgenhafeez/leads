#!/usr/bin/env python
import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

# Find all admin.py files
import glob
admin_files = glob.glob('*/admin.py')
print("Found admin.py files:", admin_files)

# Print content of each admin.py
for admin_file in admin_files:
    print(f"\n--- Content of {admin_file} ---")
    try:
        with open(admin_file, 'r') as f:
            print(f.read())
    except Exception as e:
        print(f"Error reading {admin_file}: {e}")

# Check how models are registered in admin
from django.contrib import admin
print("\n--- Registered models in admin ---")
for model, admin_obj in admin.site._registry.items():
    print(f"- {model._meta.app_label}.{model._meta.model_name}: {type(admin_obj).__name__}")
