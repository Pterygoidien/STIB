from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    DetailView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from alerts.models import Alert


# Create your views here.
def index(request):
    return render(request, 'manager/index.html')

class AlertView(ListView):
    template_name = 'manager/alert_view.html'
    context_object_name = 'alerts'

    def get_queryset(self):
        return Alert.objects.order_by('-alert_timestamp')[:50]

class UpdateAlertView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'manager/create_update.html'
    model = Alert
    fields = ['alert_station', 'alert_line', 'alert_time', 'alert_day', 'alert_remarks']

    def form_valid(self, form):
        form.instance.alert_whistleblower = self.request.user
        return super().form_valid(form)

    def test_func(self):
        alert = self.get_object()
        if self.request.user == alert.alert_whistleblower:
            return True
        return False

class AlertDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Alert
    template_name = 'manager/alert_delete.html'
    def test_func(self):
        alert = self.get_object()
        if self.request.user == alert.alert_whistleblower:
            return True
        return False



class CreateStationView(LoginRequiredMixin, CreateView):
    template_name = 'alerts/station_create.html'
    model = Alert
    fields = ['alert_station', 'alert_line', 'alert_time', 'alert_day', 'alert_remarks']

    def form_valid(self, form):
        form.instance.alert_whistleblower = self.request.user
        return super().form_valid(form)
