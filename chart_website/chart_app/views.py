
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ChartForm
from .models import ChartData
from .utils import generate_chart
from django.template import loader
from django.views import generic, View
from django.utils import timezone
import json


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'chart_app/index.html'
    context_object_name = 'latest_charts_list'
    
    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        #return ChartData.objects.order_by('-pub_date')[:5]
        return ChartData.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

 


