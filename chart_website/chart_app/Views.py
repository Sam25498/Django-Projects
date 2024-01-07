from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ChartForm
from .models import ChartData
from .utils import generate_chart
from django.template import loader


