import matplotlib.pyplot as plt
from django.shortcuts import render, redirect
from .forms import DataForm
from .models import UserInput
import json

def visualize_data(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            data = json.loads(form.cleaned_data['data'])
            chart_type = form.cleaned_data['chart_type']

            # Process structured data and generate chart based on chart_type
            # Example using Matplotlib for a bar chart
            columns = list(data[0].keys())
            values = {col: [row[col] for row in data] for col in columns}

