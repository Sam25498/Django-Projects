
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

    
    
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
import matplotlib
from matplotlib import rcParams
import matplotlib.ticker as mtick

import matplotlib.pyplot as plt
from io import BytesIO
import seaborn as sns
import base64
import json

from .models import ChartData


class GenerateChartView(View):
    template_name = 'chart_app/generate_chart.html'

    def get(self, request, *args, **kwargs):
        try:
            # Extract data_title from the URL
            data_title = kwargs.get('data_title')

            if data_title:
                # Assuming you want to retrieve the data for a specific data_title
                chart_data_instance = ChartData.objects.filter(data_title=data_title).first()

                if chart_data_instance:
                    data_title = chart_data_instance.data_title
                    
                    chart_type = chart_data_instance.chart_type

                    # Accessing the actual data attribute
                    data_string = chart_data_instance.data
                    matplotlib.use('Agg')

                    # Check if the data_string is not empty
                    if data_string:
                        try:
                            # Convert the string to a dictionary
                            diction = json.loads(data_string)

                            # Extract keys and values from the dictionary
                            
                            
                            color = diction["color"]
                            
                            title = diction["Title"]
                            subtitle = diction["SubTitle"]
                            
                            yformat = diction["y-axis in % format"]
                            
                            

                            # Plotting based on chart_type
                            if chart_type == 'Line Chart':
                                x = diction.get('X', [])
                                y = diction.get('Y', [])
                                xlabel = diction["xlabel"]
                                ylabel = diction["ylabel"]
                                fig, ax = plt.subplots()
                                ax.plot(x, y, linewidth=3)
                                sns.despine(top=True, right=True, left=True, bottom=True, offset=None, trim=False)
                                plt.grid(axis = 'y', color = 'black', linestyle = 'dotted', linewidth = 0.5)
                                plt.xlabel(xlabel)
                                plt.ylabel(ylabel)
                                
                                if title != "None":
                                    fig.suptitle(title, x=0.36,y=0.98, fontweight = "bold", fontsize= 'x-large' )#fontsize=12
                                if subtitle != "None":
                                    # Adding Title of chart
                                    plt.title(subtitle, style = "normal", x=0.26)
                                
                                #formatting the y-axis to percentage
                                if yformat == "True":
                                 
                                    ax.plot()
                                    plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter())
                                
                            elif chart_type == 'Bar Chart':
                                x = diction.get('X', [])
                                y = diction.get('Y', [])
                                xlabel = diction["xlabel"]
                                ylabel = diction["ylabel"]
                                fig, ax = plt.subplots()#figsize=(8, 8)
                                ax.bar(x, y, color=color)
                                sns.despine(top=True, right=True, left=True, bottom=False, offset=None, trim=False)
                                plt.grid(axis = 'y', color = 'black', linestyle = 'dotted', linewidth = 0.5)
                                plt.xlabel(xlabel)
                                plt.ylabel(ylabel)
                                
                                if title != "None":
                                    fig.suptitle(title, x=0.24,y=0.98, fontweight = "bold", fontsize= 'xx-large')#fontsize=12 , fontfamily = {'Oswald', 'oswald-medium','cursive', 'fantasy', 'monospace'}
                                
                                if subtitle != "None":
                                    # Adding Title of chart
                                    plt.title(subtitle, style = "normal", x=0.26)#loc="left"
                                
                                #formatting the y-axis to percentage
                                if yformat == "True":
                                 
                                    ax.plot()
                                    plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter())
                             
                                
                            elif chart_type == 'Horizontal Bar Chart':
                                x = diction.get('X', [])
                                y = diction.get('Y', [])
                                xlabel = diction["xlabel"]
                                ylabel = diction["ylabel"]
                                fig, ax = plt.subplots(figsize = (11,6))#figsize = (9, 6)
                                ax.barh(y, x, color=color)
                                sns.despine(top=True, right=True, left=True, bottom=True, offset=None, trim=False)
                                #plt.grid(axis = 'y', color = 'black', linestyle = 'dotted', linewidth = 0.5)
                                #plt.xticks(rotation = 45, fontsize = 13)
                                plt.yticks(fontsize = 13)
                                plt.xlabel(xlabel, fontsize = 13)#, fontsize = 13
                                plt.ylabel(ylabel, fontsize = 13)#, fontsize = 13
                                
                                if title != "None":
                                    fig.suptitle(title, x=0.36,y=0.98, fontweight = "bold", fontsize= 'xx-large')#fontsize=12 , fontfamily = {'Oswald', 'oswald-medium','cursive', 'fantasy', 'monospace'}
                                
                                
                                
                                if subtitle != "None":
                                    # Adding Title of chart
                                    plt.title(subtitle, style = "normal", x=0.26)#loc="left"
                                    
                                plt.subplots_adjust(left=0.12, bottom=0.1, right=0.75)
                                #formatting the y-axis to percentage
                                if yformat == "True":
                                 
                                    ax.plot()
                                    plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter())
                             
                            elif chart_type == 'Pie Chart':
                                x = diction.get('X', [])
                                y = diction.get('Y', [])
                                fig, ax1 = plt.subplots()
                                ax1.pie(y, labels=x, autopct='%1.1f%%')                               
            
                                
                                if title != "None":
                                    fig.suptitle(title, x=0.26,y=0.98, fontweight = "bold", fontsize= 'xx-large')#fontsize=12 , rcParams['font.family'] = ['Oswald', 'oswald-medium']v
                                plt.rcParams['font.family'] = ['Oswald', 'oswald-medium']
                                
                                if subtitle != "None":
                                    # Adding Title of chart
                                    plt.title(subtitle, style = "normal", x=0.04)
                    
                            
                            elif chart_type == 'Donut Chart':
                                x = diction.get('X', [])
                                y = diction.get('Y', [])
                                # explosion
                                #xplode = len(x)
                                fig, ax1 = plt.subplots()#figsize=(8,6)
                                patches, texts, autotexts = ax1.pie(y, colors=color, labels=x,autopct='%1.1f%%',pctdistance=0.85)
                               
                                for text in texts:
                                    text.set_color('black')
                                for autotext in autotexts:
                                    autotext.set_color('white')
                                    autotext.set_fontsize(9)
                                # draw circle
                                centre_circle = plt.Circle((0, 0), 0.70, fc='white')
                                fig = plt.gcf()
 
                                # Adding Circle in Pie chart
                                fig.gca().add_artist(centre_circle)
        
                                if title != "None":
                                    fig.suptitle(title, x=0.26,y=0.98, fontweight = "bold", fontsize= 'xx-large')#fontsize=12 , rcParams['font.family'] = ['Oswald', 'oswald-medium']v
                                plt.rcParams['font.family'] = ['Oswald', 'oswald-medium']
                                
                                if subtitle != "None":
                                    # Adding Title of chart
                                    plt.title(subtitle, style = "normal", x=0.04)
                    
                                plt.legend(bbox_to_anchor=(1,0), loc="lower right", 
                          bbox_transform=plt.gcf().transFigure)#, bbox_to_anchor=(0.9, 0.1)
        
        
 

                                
                                
                            elif chart_type == 'Bar and Line Chart':
                                x = diction.get('X', [])
                                y_line = diction.get("Y_Line", [])
                                y_bar = diction.get("Y_Bar", [])
                            

                                color_line = diction["color_Line"]
                                #color_bar = diction["color_Bar"]
                                
                                xlabel = diction["xlabel"]
                                ylabel_bar = diction["ylabel_Bar"]                                
                                ylabel_line = diction["ylabel_Line"]
                                
                                fig, ax1 = plt.subplots()
                                ax1.bar(x, y_bar, label='Bar Chart', color = color)
                                ax1.plot(x, y_line, label='Line Chart', color= color_line)
                                sns.despine(top=True, right=True, left=True, bottom=False, offset=None, trim=False)
                                ax1.set_axisbelow(True)
                                ax1.grid(axis = 'y', color = 'black', linestyle = 'dotted', linewidth = 0.5)
                                plt.xlabel(xlabel)
                                plt.ylabel(ylabel_bar)
                                plt.ylabel(ylabel_line)
                                #plt.legend()
                                if title != "None":
                                    fig.suptitle(title, y=0.98, fontweight = "bold", fontsize= 'x-large' , horizontalalignment ='center')#fontsize=12 x=0.40,
                                if subtitle != "None":
                                    # Adding Title of chart
                                    plt.title(subtitle, style = "normal",  horizontalalignment ='center')#x=0.18,
                                
                                #formatting the y-axis to percentage
                                if yformat == "True":
                                 
                                    ax1.plot()
                                    plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter())
                                
                            # Adding Title of chart
                            #plt.title(title, loc='left',fontsize=12, style = "bold")
                            #plt.suptitle(subtitle, loc= 'left')#fontsize=12
                            

                            # Save the plot to a BytesIO object with a specified DPI (e.g., 300)
                            dpi = 300
                            image_stream = BytesIO()
                            plt.savefig(image_stream, format='png', dpi=dpi)
                            plt.close()

                            # Encode the image stream to base64
                            image_base64 = base64.b64encode(image_stream.getvalue()).decode('utf-8')

                            context = {'image_base64': image_base64}
                            return render(request, self.template_name, context)

                        except json.JSONDecodeError as json_error:
                            return HttpResponse(f"Error decoding JSON: {json_error}")

                    else:
                        return HttpResponse("Data string is empty.")

                else:
                    return HttpResponse(f"No ChartData instance found for data_title: {data_title}")

            else:
                return HttpResponse("No data_title provided in the URL.")

        except Exception as e:
            return HttpResponse(f"An unexpected error occurred: {e}")
        



