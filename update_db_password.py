#!/usr/bin/env python3
import re

with open('config/settings.py', 'r') as f:
    content = f.read()

# Look for the database password pattern and replace it
if "'PASSWORD':" in content:
    content = re.sub(r"'PASSWORD':\s*'[^']*'", "'PASSWORD': 'leads_password'", content)
else:
    # If we can't find the pattern, add the complete DATABASES setting
    db_settings = """
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'leads',
        'USER': 'leads_user',
        'PASSWORD': 'leads_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
"""
    if 'DATABASES' not in content:
        content += "\n" + db_settings

with open('config/settings.py', 'w') as f:
    f.write(content)

print("Database password updated in settings.py")
