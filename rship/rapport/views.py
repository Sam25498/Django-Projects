from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from .models import Description


# Create your views here.
def index(request):
    #'-event_date' orders the items in reverse
    latest_description_list = Description.objects.order_by('event_date')[:5]
    template = loader.get_template('rapport/index.html')
    context = {
        'latest_description_list' : latest_description_list,
    }
    return HttpResponse(template.render(context, request))

def demo(request):
    results = test_calendar()
    context = {"results": results}
    return render(request, 'demo.html', context)
