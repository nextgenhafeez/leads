
# Monkey patch the get_app_list method of AdminSite to put User model at the top
from django.contrib.admin.sites import AdminSite

# Store the original method
original_get_app_list = AdminSite.get_app_list

def custom_get_app_list(self, request):
    """
    Custom get_app_list method that puts the User model at the top of the USERS section
    """
    app_list = original_get_app_list(self, request)
    
    # Find the users app
    for app in app_list:
        if app['app_label'] == 'users':
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

# Replace the method
AdminSite.get_app_list = custom_get_app_list
