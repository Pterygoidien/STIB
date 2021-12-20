from django.urls import path
from . import views

app_name='profiles'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('id/<int:pk>/',views.profileDetail.as_view(), name='detail-id'),
    path('username/<str:username>/', views.profileDetail.as_view(), name='detail-username'),

]