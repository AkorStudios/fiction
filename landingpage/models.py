from django.db import models

# Create your models here.

class EarlyUser(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    storytype = models.CharField(max_length=200, null=False, blank=False)
    phone = models.CharField(max_length=200, null=False, blank=False)
    
    def __str__(self):
        return self.name [:200]