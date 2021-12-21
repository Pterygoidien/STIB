from django import forms
from .models import Station
from django.contrib.admin import widgets


class StationForm(forms.Form):
    departure = forms.ModelChoiceField(
        queryset=Station.objects.all().order_by('Station_name'),
        empty_label=None,
        label='Arrêt de départ'
    )
    arrival = forms.ModelChoiceField(
        queryset=Station.objects.all().order_by('Station_name'),
        empty_label=None,
        label='Arrêt d\'arrivée'
    )
