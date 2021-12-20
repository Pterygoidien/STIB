from django.urls import path
from .views import (
    IndexView,
    CreateAlertView,
    UpdateAlertView,
    AlertDetail,
    AlertDelete
)

app_name='alerts'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', AlertDetail.as_view(), name='detail'),
    path('add/', CreateAlertView.as_view(), name='add'),
    path('<int:pk>/update/', UpdateAlertView.as_view(), name='update'),
    path('<int:pk>/delete/', AlertDelete.as_view(), name='delete'),
]