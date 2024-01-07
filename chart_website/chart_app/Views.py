from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ChartForm
from .models import ChartData
from .utils import generate_chart
from django.template import loader

def index(request):
    latest_charts_list = ChartData.objects.order_by('-pub_date')[:5]
    template = loader.get_template('chart_app/index.html')
    context = {
        'latest_charts_list': latest_charts_list,
    }
    return HttpResponse(template.render(context, request))
    





