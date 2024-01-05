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

            for col, values_list in values.items():
                plt.bar(range(len(values_list)), values_list, label=col)

            plt.title('User-generated Bar Chart')
            plt.xlabel('X-axis')
            plt.ylabel('Y-axis')
            plt.legend()
            
            chart_path = 'dataviz/static/dataviz/chart.png'
            plt.savefig(chart_path)  # Save chart as a static file

            # Save user input data
            form.save()

            return render(request, 'dataviz/visualization.html', {'chart_path': chart_path})
    else:
        form = DataForm()

    return render(request, 'dataviz/index.html', {'form': form})
