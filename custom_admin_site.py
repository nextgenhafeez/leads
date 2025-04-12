
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Create a custom AdminSite
class CustomAdminSite(admin.AdminSite):
    def get_app_list(self, request):
        app_list = super().get_app_list(request)
        
        # Find the app with the USERS section
        for app in app_list:
            if app.get('name') == 'USERS' or app.get('app_label') == 'auth':
                # Get the models in this app
                models = app['models']
                
                # Find the User model
                user_model = None
                for i, model in enumerate(models):
                    if model['object_name'] == 'User':
                        user_model = models.pop(i)
                        break
                
                # If we found the User model, put it at the beginning
                if user_model:
                    models.insert(0, user_model)
                    app['models'] = models
        
        return app_list

# Create a new admin site
custom_site = CustomAdminSite(name='custom_admin')

# Register all models from the default admin site to our custom one
for model, model_admin in list(admin.site._registry.items()):
    if model == User:
        # Register User with the default UserAdmin
        custom_site.register(User, UserAdmin)
    else:
        # Register all other models with their current admin
        custom_site.register(model, type(model_admin))

# Replace the default admin site
admin.site = custom_site
admin.sites.site = custom_site
