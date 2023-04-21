from django.db import models

class EducationModul(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=250)
