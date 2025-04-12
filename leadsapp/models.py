from django.db import models
from django.conf import settings
from django.contrib.auth.models import User  # Use Django's built-in User model

# All your existing models go here, but NOT the custom User model

class Activity(models.Model):
    lead = models.ForeignKey('Lead', on_delete=models.CASCADE)
    agent = models.ForeignKey('Agent', on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "activities"

    def __str__(self):
        return f"{self.activity_type} - {self.lead.name}"

class Agent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Company(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "companies"

    def __str__(self):
        return self.name

class Files(models.Model):
    lead = models.ForeignKey('Lead', on_delete=models.CASCADE)
    file = models.FileField(upload_to='lead_files/')
    description = models.TextField(blank=True, null=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "files"

    def __str__(self):
        return f"{self.lead.name} - {self.description}"

class Followups(models.Model):
    lead = models.ForeignKey('Lead', on_delete=models.CASCADE)
    agent = models.ForeignKey('Agent', on_delete=models.CASCADE)
    date = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "followups"

    def __str__(self):
        return f"{self.lead.name} - {self.date}"

class Form(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Invitation(models.Model):
    email = models.EmailField()
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    invited_by = models.ForeignKey(User, on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    source = models.ForeignKey('Source', on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=50, default='New')
    assigned_to = models.ForeignKey('Agent', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class LeadsGroup(models.Model):
    name = models.CharField(max_length=100)
    leads = models.ManyToManyField('Lead')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Messages(models.Model):
    lead = models.ForeignKey('Lead', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "messages"

    def __str__(self):
        return f"{self.lead.name} - {self.created_at}"

class Source(models.Model):
    name = models.CharField(max_length=100)
    source_type = models.ForeignKey('SourceType', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class SourceType(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
