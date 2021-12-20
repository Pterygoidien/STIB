from django.shortcuts import render
from django.views import generic
from alerts.models import Alert

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
        return Alert.objects.order_by('-alert_timestamp')[:10]

