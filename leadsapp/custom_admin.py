from django.contrib import admin
from django.apps import apps
from allauth.account.models import EmailAddress

# First, try to unregister EmailAddress if it's already registered
try:
    admin.site.unregister(EmailAddress)
except admin.sites.NotRegistered:
    pass  # It's not registered, which is fine

# Now register all models from leadsapp
from .models import (
    Lead,
    Company,
    Agent,
    SourceType,
    Source,
    LeadsGroup,
    Activity,
    Messages,
    Files,
    Followups,
    Form,
    Invitation,
)

# Register models
admin.site.register(Lead)
admin.site.register(Company)
admin.site.register(Agent)
admin.site.register(SourceType)
admin.site.register(Source)
admin.site.register(LeadsGroup)
admin.site.register(Activity)
admin.site.register(Messages)
admin.site.register(Files)
admin.site.register(Followups)
admin.site.register(Form)
admin.site.register(Invitation)

# Re-register EmailAddress with a custom admin class
class EmailAddressAdmin(admin.ModelAdmin):
    list_display = ('email', 'user', 'primary', 'verified')
    search_fields = ('email', 'user__username')
    list_filter = ('primary', 'verified')

admin.site.register(EmailAddress, EmailAddressAdmin)
