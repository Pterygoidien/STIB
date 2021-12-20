from django.shortcuts import render
from django.views import generic
from alerts.models import Alert

class IndexView(generic.ListView):
    template_name = 'alerts/index.html'
    context_object_name = 'alerts'

    def get_queryset(self):
        return Alert.objects.order_by('-alert_timestamp')[:10]

def createAlert(request):
    return render(request, 'alerts/alertform.html')

class AlertDetail(generic.DetailView):
    model = Alert
    template_name = 'alerts/detail.html'