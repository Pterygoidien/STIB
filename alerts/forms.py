from django import forms
from .models import Alert
from transports.models import Station, Line
from django.utils.translation import gettext_lazy as _
from django.contrib.admin import widgets



#station_choices = ((pk, station_name))
class AlertForm(forms.ModelForm):

    class Meta:
        model = Alert
        fields = ['alert_station', 'alert_line', 'alert_time']
        labels = {
            'alert_station': _('Arrêt de bus concerné'),
            'alert_line': _('Ligne de bus'),
            'alert_time':_('L\'heure de survenue')
        }



class SearchAlert_Station(forms.Form):
    station = forms.ModelChoiceField(
        queryset=Station.objects.all(),
        empty_label='Sélectionnez un arrêt',
        label=None,
        required=False
    )

class SearchAlert_Line(forms.Form):
    line = forms.ModelChoiceField(
        queryset=Line.objects.all(),
        empty_label='Sélectionnez une ligne',
        label=None,
        required=False
    )



