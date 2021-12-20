from django.shortcuts import render
from django.views import generic
from alerts.models import Alert
from datetime import date

def index(request):
    context = {
        'title':'Page d\'accueil',
        'alerts':Alert.objects.order_by('-alert_timestamp')[:5]
    }
    return render(request, 'main/index.html', context)


class IndexView(generic.ListView):
    template_name = 'main/index.html'
    context_object_name = 'alerts'

    def get_queryset(self):
        return Alert.objects.filter(alert_day=date.today()).order_by('-alert_time')[:10]

