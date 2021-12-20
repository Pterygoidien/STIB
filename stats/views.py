from django.shortcuts import render
from django.views import generic
from alerts.models import Alert


def index(request):
    return render(request, 'stats/index.html')