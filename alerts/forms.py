from django import forms
from transports.models import Station, Line
import datetime


#station_choices = ((pk, station_name))
class AlertForm(forms.Form):

    alert_stations = forms.ModelChoiceField(queryset = Station.objects.all())
    alert_line = forms.ModelChoiceField(queryset=Line.objects.all())
    '''alert_timestamp = forms.DateTimeField(
        label='Date et heure',
        input_formats=["%d/%m/%Y %H:%M:%S"],
        required=True,
        widget=forms.DateTimeInput(
            attrs={'type':'datetime',
                   'required pattern':'[0-9]{2}/[0-9]{2}/[0-9]{4}',
                   'placeholder':datetime.datetime.now,
                   })
    )'''
    #En construction
