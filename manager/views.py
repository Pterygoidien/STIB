from django.shortcuts import render
from django.views import generic
from alerts.models import Alert


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'manager/index.html'
    context_object_name = 'alerts'

    def get_queryset(self):
        return Alert.objects.order_by('-alert_timestamp')[:10]

def index(request):
    return render(request, 'manager/index.html')