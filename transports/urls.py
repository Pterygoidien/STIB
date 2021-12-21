from django.urls import path
from .views import SearchItinary

app_name='transports'
urlpatterns = [
    path('itinary/', SearchItinary, name='itinary'),


]