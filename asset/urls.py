
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('companies/', views.company_list, name='company_list'),
    path('companies/<int:company_id>/employees/', views.employee_list, name='employee_list'),
    path('devices/', views.device_list, name='device_list'),
    path('devices/<int:device_id>/checkout/', views.device_checkout, name='device_checkout'),
    path('devices/<int:device_id>/checkin/', views.device_checkin, name='device_checkin'),
]
