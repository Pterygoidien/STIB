from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.views.generic import (
    DetailView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from .forms import (
    AlertForm,
    SearchAlert_Station,
    SearchAlert_Line
)
from alerts.models import Alert


def SearchAlerts(request):
    context = {
        'form_line':SearchAlert_Line(),
        'form_station':SearchAlert_Station(),
        'results':[]
    }
    if request.method == 'GET':
        form_line = SearchAlert_Line(request.GET)
        form_station=SearchAlert_Station(request.GET)
        if form_line.is_valid() and form_station.is_valid():
            context['form_line'], context['form_station'] = form_line, form_station

            if 'line' in request.GET:
                cleaned_form = form_line.cleaned_data
                line = cleaned_form['line']
                try:
                    alerts=Alert.objects.all().filter(alert_line__id=line.id)
                    if alerts:
                        context['results'].append(alerts)
                except(KeyError, Alert.DoesNotExist):
                    messages.error('Aucune instance trouvée')
            if 'station' in request.GET:
                cleaned_form = form_station.cleaned_data
                station = cleaned_form['station']
                try:
                    alerts=Alert.objects.all().filter(alert_station__id=station.id)
                    if alerts:
                        context['results'].append(alerts)
                except(KeyError, Alert.DoesNotExist):
                    messages.error('Aucune instance trouvée')
    return render(request, 'alerts/search.html', context)


class IndexView(ListView):
    model = Alert
    template_name = 'alerts/index.html'
    context_object_name = 'alerts'
    ordering = ['-alert_timestamp']
    paginate_by = 10


class AlertDetail(DetailView):
    model = Alert
    template_name = 'alerts/detail.html'


class CreateAlertView(LoginRequiredMixin, CreateView):
    template_name = 'alerts/create.html'
    model = Alert
    fields = ['alert_station', 'alert_line', 'alert_time', 'alert_remarks']
    class Meta:
        labels = {
            'alert_station': _('Arrêt de bus concerné'),
            'alert_line': _('Ligne de bus'),
            'alert_time': _('L\'heure de survenue')
        }

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

