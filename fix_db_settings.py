#!/usr/bin/env python3
import re

with open('config/settings.py', 'r') as f:
    content = f.read()

# Update the database settings to match the original deployment
db_settings = """
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'leads',
        'USER': 'leads_user',
        'PASSWORD': 'your_original_password',  # Replace with the original password
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
"""

# Check if DATABASES is in the content
if 'DATABASES' in content:
    # Replace the existing DATABASES configuration
    content = re.sub(r'DATABASES\s*=\s*{.*?}', db_settings, content, flags=re.DOTALL)
else:
    # Add the DATABASES configuration at the end
    content += "\n" + db_settings

# Write the updated content back to settings.py
with open('config/settings.py', 'w') as f:
    f.write(content)

print("Database settings updated")
