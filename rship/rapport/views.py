from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from .models import Description

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'rapport/index.html'
    context_object_name = 'description_list'
    
    def get_queryset(self):
        """Return the last five keyed entries"""
        return Description.objects.order_by('-event_date')[:5]
