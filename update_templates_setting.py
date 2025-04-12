#!/usr/bin/env python3
import re

with open('config/settings.py', 'r') as f:
    content = f.read()

# Make sure os is imported
if "import os" not in content:
    content = "import os\n" + content

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

# Write the updated content back to settings.py
with open('config/settings.py', 'w') as f:
    f.write(content)

print("Updated templates setting in settings.py")
