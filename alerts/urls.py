from django.urls import path
from . import views

app_name='alerts'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add/', views.createAlert, name='create'),
    path('<int:pk>/', views.AlertDetail.as_view(), name='detail')


]