from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    DetailView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from .forms import AlertForm
from alerts.models import Alert


class IndexView(ListView):
    model = Alert
    template_name = 'alerts/index.html'
    context_object_name = 'alerts'
    ordering = ['-alert_timestamp']
    paginate_by = 10


class AlertDetail(DetailView):
    model = Alert
    template_name = 'alerts/detail.html'

#Alternate form
def createAlert(request):
    if request.method == 'POST':
        form = AlertForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Alerte créée')
            return redirect('alerts:index')
    else:
        form = AlertForm()

    return render(request, 'alerts/create.html', {'form':form})


class CreateAlertView(LoginRequiredMixin, CreateView):
    template_name = 'alerts/create.html'
    model = Alert
    fields = ['alert_station', 'alert_line', 'alert_time', 'alert_day', 'alert_remarks']

    def form_valid(self, form):
        form.instance.alert_whistleblower = self.request.user
        return super().form_valid(form)

class UpdateAlertView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'alerts/create.html'
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
    template_name = 'alerts/delete.html'
    def test_func(self):
        alert = self.get_object()
        if self.request.user == alert.alert_whistleblower:
            return True
        return False