from django.db import models

class UserInput(models.Model):
    data = models.JSONField()
    chart_type = models.CharField(max_length=50)
