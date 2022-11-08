from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import datetime

# Create your models here.
class Description(models.Model):
    title = models.CharField(max_length=200)
    description_text = models.TextField(max_length=400, help_text='Enter a brief description of your entry' )
    reminder_date = models.DateTimeField('date to be reminded')
    event_date = models.DateTimeField('date of event')
    
    def __str__(self):
        return self.title #, #self.reminder_date, self.event_date
    
    def is_upcoming(self):
        return self.event_date <= timezone.now() + datetime.timedelta(days=30)
    
    def get_absolute_url(self):
        """Returns the URL to access a detail record of this description."""
        return reverse('description-detail', args=[str(self.id)])
    
    class Meta:
        ordering = ['event_date']
