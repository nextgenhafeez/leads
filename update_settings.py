#!/usr/bin/env python3
import re

with open('config/settings.py', 'r') as f:
    content = f.read()

# Make sure required imports are present
if "import os" not in content:
    content = "import os\n" + content

# Make sure DEBUG is False for production
if "DEBUG = True" in content:
    content = content.replace("DEBUG = True", "DEBUG = False")

# Make sure ALLOWED_HOSTS includes your domain
if "ALLOWED_HOSTS" in content:
    if "blacklayer.app" not in content and "'*'" not in content and '"*"' not in content:
        content = re.sub(r'ALLOWED_HOSTS\s*=\s*\[(.*?)\]', r'ALLOWED_HOSTS = [\1, "blacklayer.app"]', content, flags=re.DOTALL)
else:
    content += '\nALLOWED_HOSTS = ["blacklayer.app", "localhost", "127.0.0.1"]\n'

# Add django-allauth to INSTALLED_APPS if not already there
if "'allauth'" not in content and '"allauth"' not in content:
    # Find the INSTALLED_APPS list
    pattern = r'INSTALLED_APPS\s*=\s*\[(.*?)\]'
    # Add allauth apps to INSTALLED_APPS
    replacement = lambda m: m.group(0).replace(']', ",\n    'django.contrib.sites',\n    'allauth',\n    'allauth.account',\n    'allauth.socialaccount',\n]")
    content = re.sub(pattern, replacement, content, flags=re.DOTALL)

# Add SITE_ID if not already there
if "SITE_ID = 1" not in content:
    # Add SITE_ID at the end of the file
    content += "\n\n# Django AllAuth Configuration\nSITE_ID = 1\n"

# Add authentication backends if not already there
if "AUTHENTICATION_BACKENDS" not in content:
    # Add authentication backends at the end of the file
    content += """
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]
"""

# Add AllAuth settings if not already there
if "ACCOUNT_EMAIL_REQUIRED" not in content:
    # Add AllAuth settings at the end of the file
    content += """
# AllAuth settings
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
LOGIN_REDIRECT_URL = '/accounts/profile/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
"""

# Make sure TEMPLATES is correctly configured
if "TEMPLATES" in content:
    # Check if 'DIRS' includes our templates directory
    if "'templates'" not in content and '"templates"' not in content:
        content = re.sub(
            r"('DIRS':\s*\[)(.*?)(\])",
            r"\1os.path.join(BASE_DIR, 'templates'), \2\3",
            content,
            flags=re.DOTALL
        )
else:
    # Add TEMPLATES setting at the end of the file
    content += """
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
"""

# Make sure STATIC_URL and STATIC_ROOT are defined
if "STATIC_URL" not in content:
    content += "\nSTATIC_URL = '/static/'\n"
if "STATIC_ROOT" not in content:
    content += "\nSTATIC_ROOT = os.path.join(BASE_DIR, 'static')\n"

# Write the updated content back to settings.py
with open('config/settings.py', 'w') as f:
    f.write(content)

print("Updated settings.py file")
