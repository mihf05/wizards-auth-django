from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class APIKey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='api_keys')
    key = models.CharField(max_length=64, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"API Key for {self.user.username}"

    def is_valid(self):
        return self.is_active and (self.expires_at is None or self.expires_at > timezone.now())

# We don't need to create a custom model for login history
# as django-login-history2 provides the LoginHistory model automatically

class LoginToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='login_tokens')
    token = models.CharField(max_length=64, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Login Token for {self.user.username}"

    def is_valid(self):
        # Token is valid for 15 minutes
        return self.is_active and (timezone.now() - self.created_at).total_seconds() < 900
