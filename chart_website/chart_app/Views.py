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

def chart_input(request):
    if request.method == 'POST':
        form = ChartForm(request.POST)
        if form.is_valid():
            data_type = form.cleaned_data['data_type']
            chart_type = form.cleaned_data['chart_type']
            data_input = form.cleaned_data['data_input']


             chart_data = ChartData(data_type=data_type, chart_type=chart_type, data=data_input)
            chart_data.save()

            generate_chart(data_type, chart_type, data_input)

            return redirect('chart_output')
    else:
        form = ChartForm()

    return render(request, 'chart_app/chart_input.html', {'form': form})







