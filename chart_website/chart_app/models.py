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
    
chart_type = models.CharField(max_length=20, choices=CHART_TYPE_CHOICES)
    data = models.TextField(default='{}')  # Set default to an empty dictionary
    pub_date = models.DateTimeField('date published',default=timezone.now)
   
    def save_data(self, data_dict):
        # Convert the Python dictionary to a JSON-formatted string
        self.data = json.dumps(data_dict)
        self.save()
      
