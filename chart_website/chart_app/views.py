
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

 
class ChartDetailView(generic.DetailView):
    model = ChartData
    template_name = 'chart_app/chart_detail.html'
    context_object_name = 'chart_data'
    slug_field = 'data_title'
    slug_url_kwarg = 'data_title'

   
from django.shortcuts import render, redirect
from django.views import View
from .models import ChartData
from .forms import ChartForm

class AddChartView(View):
    template_name = 'chart_app/add_chart.html'

    def get(self, request):
        form = ChartForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ChartForm(request.POST)

        if form.is_valid():
            # Create a new ChartData instance
            chart_data = ChartData(
                data_title=form.cleaned_data['data_title'],
                data_type=form.cleaned_data['data_type'],
                chart_type=form.cleaned_data['chart_type'],
            )

            # Example data dictionary
            data_dict = {
                'name': 'John',
                'Axis Titles': ['Time', 'Price'],
                'X': ['Standard Class', 'First Class', 'Second Class', 'Same Day'],
                'Y': [3200, 3000, 2800, 1000],
                'xlabel': 'Principal Component', 
                'ylabel': 'Cumulative Explained Variance', 
                'color': 'blue'
            }

            # Use the save_data method to save the data
            chart_data.save_data(data_dict)

            return redirect('chart_app:index')

        return render(request, self.template_name, {'form': form})

    
    



