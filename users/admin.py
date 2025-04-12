from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Unregister the default User admin if it's registered
try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass

# Register User with a custom admin to make it appear first
class CustomUserAdmin(UserAdmin):
    # This is a trick to make it appear at the top of the USERS section
    def get_model_perms(self, request):
        perms = super().get_model_perms(request)
        # This ensures it appears at the top when sorted
        perms['_order'] = 0
        return perms

# Register User with our custom admin
admin.site.register(User, CustomUserAdmin)

# Register other models below


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

# Register User first
admin.site.register(User)

# Then register other models
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
