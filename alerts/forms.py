from django import forms
from .models import Alert
from django.contrib.admin import widgets



#station_choices = ((pk, station_name))
class AlertForm(forms.ModelForm):

    class Meta:
        model = Alert
        fields = ['alert_station', 'alert_line']


