from django import forms
from .models import Station
from django.contrib.admin import widgets


class StationForm(forms.Form):
    departure = forms.ModelChoiceField(
        queryset=Station.objects.all(),
        empty_label='Sélectionnez un arrêt',
        label='Arrêt de départ'
    )
    arrival = forms.ModelChoiceField(
        queryset=Station.objects.all(),
        empty_label='Sélectionnez un arrêt',
        label='Arrêt d\'arrivée'
    )
