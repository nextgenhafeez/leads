#!/usr/bin/env python
import os

# Path to the users/admin.py file
users_admin_file = 'users/admin.py'

# New content with a custom ModelAdmin for User
new_users_admin_content = """from django.contrib import admin

class UserAdmin(admin.ModelAdmin):
    # This will make it appear at the top
    list_display = ['email', 'first_name', 'last_name']
    
    # This is a hack to make it appear at the top
    # The admin sorts by this field, so we'll give it a value that sorts first
    def get_model_perms(self, request):
        perms = super().get_model_perms(request)
        perms['__first__'] = True
        return perms

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

# Register User with the custom admin
admin.site.register(User, UserAdmin)

# Register other models
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
if not os.path.exists(users_admin_file):
    print(f"Error: {users_admin_file} not found")
    exit(1)

# Write the new content
with open(users_admin_file, 'w') as f:
    f.write(new_users_admin_content)
    print(f"Updated {users_admin_file} with custom UserAdmin")
