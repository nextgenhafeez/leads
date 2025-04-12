#!/usr/bin/env python
import os

# Path to the admin.py file
admin_file = 'users/admin.py'

# New content with the desired order
new_content = """from django.contrib import admin

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

# Register models in the desired order
admin.site.register(User)  # Register Users first
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

# Check if file exists
if not os.path.exists(admin_file):
    print(f"Error: {admin_file} not found")
    exit(1)

# Write the new content
with open(admin_file, 'w') as f:
    f.write(new_content)
    print(f"Updated {admin_file} with the desired registration order")
