from django.urls import path
from .views import (
    index,
    AlertView,
    UpdateAlertView,
    AlertDelete


)

app_name='manager'
urlpatterns = [
    path('', index, name='index'),
    path('alerts/', AlertView.as_view(), name="alert-view"),
    path('alerts/delete/<int:pk>/', AlertDelete.as_view(), name="alert-delete"),
    path('alerts/update/<int:pk>/', AlertDelete.as_view(), name="alert-update"),





]