#!/usr/bin/env python3
import re

# Read the current urls.py file
with open('config/urls.py', 'r') as f:
    content = f.read()

# Make sure the necessary imports are there
if 'from django.views.generic import RedirectView' not in content:
    content = re.sub(
        r'from django.urls import (.*)',
        r'from django.urls import \1\nfrom django.views.generic import RedirectView',
        content
    )

# Make sure the home view is imported
if 'from leadsapp.views import home_view' not in content:
    if 'from leadsapp.views import' in content:
        content = re.sub(
            r'from leadsapp.views import (.*)',
            r'from leadsapp.views import \1, home_view',
            content
        )
    else:
        content = re.sub(
            r'from django.urls import (.*)',
            r'from django.urls import \1\nfrom leadsapp.views import home_view',
            content
        )

# Make sure the profile view is imported
if 'profile_view' not in content:
    if 'from leadsapp.views import' in content:
        content = re.sub(
            r'from leadsapp.views import (.*)',
            r'from leadsapp.views import \1, profile_view',
            content
        )
    else:
        content = re.sub(
            r'from django.urls import (.*)',
            r'from django.urls import \1\nfrom leadsapp.views import profile_view',
            content
        )

# Make sure 'include' is imported
if 'include' not in content:
    content = re.sub(
        r'from django.urls import (.*)',
        r'from django.urls import \1, include',
        content
    )

# Make sure the home URL pattern is correct
if "path('', home_view, name='home')" not in content:
    if "path('', " in content:
        content = re.sub(
            r"path$$'', .*?, name='home'$$",
            r"path('', home_view, name='home')",
            content
        )
    else:
        # Add the home URL pattern
        content = re.sub(
            r'urlpatterns\s*=\s*\[(.*?)\]',
            r'urlpatterns = [\1\n    path("", home_view, name="home"),\n]',
            content,
            flags=re.DOTALL
        )

# Make sure the profile URL pattern is there
if "path('accounts/profile/', profile_view, name='account_profile')" not in content:
    content = re.sub(
        r'urlpatterns\s*=\s*\[(.*?)\]',
        r'urlpatterns = [\1\n    path("accounts/profile/", profile_view, name="account_profile"),\n]',
        content,
        flags=re.DOTALL
    )

# Make sure django-allauth URLs are included
if "path('accounts/', include('allauth.urls'))" not in content:
    content = re.sub(
        r'urlpatterns\s*=\s*\[(.*?)\]',
        r'urlpatterns = [\1\n    path("accounts/", include("allauth.urls")),\n]',
        content,
        flags=re.DOTALL
    )

# Write the updated content back to urls.py
with open('config/urls.py', 'w') as f:
    f.write(content)

print("Fixed urls.py file")
