from django.db import models


class Activity(models.Model):
    created_on = models.DateField(auto_now_add=True, null=True, blank=True)
    updated_on = models.DateField(auto_now=True, null=True, blank=True)
    completed = models.BooleanField(default=False)
    name = models.CharField(max_length=500, null=False, blank=False)
    desc = models.TextField(max_length=2000, default="", blank=True)
