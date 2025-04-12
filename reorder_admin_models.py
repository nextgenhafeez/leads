#!/usr/bin/env python
import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib import admin
from django.apps import apps

# First, let's see what's currently registered
print("Currently registered models:")
for model, model_admin in admin.site._registry.items():
    print(f"- {model._meta.app_label}.{model.__name__}")

# Find all models in the leadsapp
leadsapp_models = {}
for model in apps.get_models():
    if model._meta.app_label == 'leadsapp':
        leadsapp_models[model.__name__] = model

print("\nFound leadsapp models:")
for name, model in leadsapp_models.items():
    print(f"- {name}")

# Define the order we want
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

# Unregister all models from leadsapp
for name, model in leadsapp_models.items():
    if model in admin.site._registry:
        admin.site.unregister(model)
        print(f"Unregistered {name}")

# Register models in the desired order
for name in desired_order:
    if name in leadsapp_models:
        model = leadsapp_models[name]
        admin.site.register(model)
        print(f"Registered {name} in desired order")
    else:
        print(f"Model {name} not found in leadsapp")

# Now update the leadsapp/admin.py file to make this change permanent
admin_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'leadsapp', 'admin.py')
if os.path.exists(admin_file):
    print(f"\nUpdating {admin_file}")
    
    # Create new content for admin.py
    new_content = """from django.contrib import admin

# Import all models
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
    SourceType,
    Source,
    User,
)

# Register models in specific order
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
    
    # Write the new content
    with open(admin_file, 'w') as f:
        f.write(new_content)
        print(f"Updated {admin_file} with models in desired order")
else:
    print(f"\n{admin_file} not found")
    
    # Try to find the admin.py file
    for root, dirs, files in os.walk(os.path.dirname(os.path.abspath(__file__))):
        if 'admin.py' in files and 'venv' not in root and 'site-packages' not in root:
            admin_file = os.path.join(root, 'admin.py')
            print(f"Found admin.py at {admin_file}")
            
            # Read the current content
            with open(admin_file, 'r') as f:
                current_content = f.read()
                
            # Check if this is the right admin.py file
            if any(model_name in current_content for model_name in ['Activity', 'Agent', 'Lead']):
                print(f"This appears to be the right admin.py file")
                
                # Create new content for admin.py
                new_content = """from django.contrib import admin

# Import all models
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
    SourceType,
    Source,
    User,
)

# Register models in specific order
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
                
                # Write the new content
                with open(admin_file, 'w') as f:
                    f.write(new_content)
                    print(f"Updated {admin_file} with models in desired order")
                
                break
