import json
from django.db import models
from django.utils import timezone

class ChartData(models.Model):    
    data_title = models.CharField(max_length=50)
    data_type = models.CharField(max_length=50)
    # Use CharField with choices for chart_type
    CHART_TYPE_CHOICES = [
        ('Line Chart', 'Line Chart'),
        ('Bar Chart', 'Bar Chart'),
        ('Pie Chart', 'Pie Chart'),
        ('Donut Chart', 'Donut Chart'),
        ('Bar and Line Chart', 'Bar and Line Chart'),
        ('Horizontal Bar Chart','Horizontal Bar Chart'),
    ]
    
