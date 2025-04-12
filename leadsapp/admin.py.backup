from django.contrib import admin
from django.contrib.auth.models import User

# Import all models
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
    SourceType,
    Source,
)

# Register models with ModelAdmin classes
@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'status', 'created_at']
    list_filter = ['status']
    search_fields = ['name', 'email']

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'website', 'created_at']
    search_fields = ['name']

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ['user', 'company', 'created_at']

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['lead', 'agent', 'activity_type', 'created_at']
    list_filter = ['activity_type']

@admin.register(Files)
class FilesAdmin(admin.ModelAdmin):
    list_display = ['lead', 'description', 'uploaded_by', 'uploaded_at']

@admin.register(Followups)
class FollowupsAdmin(admin.ModelAdmin):
    list_display = ['lead', 'agent', 'date', 'completed']
    list_filter = ['completed']

@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_by', 'created_at']

@admin.register(Invitation)
class InvitationAdmin(admin.ModelAdmin):
    list_display = ['email', 'company', 'invited_by', 'accepted']
    list_filter = ['accepted']

@admin.register(LeadsGroup)
class LeadsGroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']

@admin.register(Messages)
class MessagesAdmin(admin.ModelAdmin):
    list_display = ['lead', 'sender', 'created_at']

@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ['name', 'source_type', 'created_at']

@admin.register(SourceType)
class SourceTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
