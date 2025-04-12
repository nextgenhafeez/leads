from django.apps import AppConfig

class LeadsappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'leadsapp'
    verbose_name = 'Lead Management'  # This will be the section title in admin
