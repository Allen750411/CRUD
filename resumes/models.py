from django.db import models


class Resume(models.Model):
    title = models.CharField(null=True, max_length=100)
    skill = models.CharField(null=True, max_length=200)
    content = models.TextField(null=True, max_length=300)
