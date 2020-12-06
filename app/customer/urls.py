from django.urls import path
from . import views

app_name = 'customer'

urlpatterns = [
    path('create/', views.CreateCustomerView.as_view(), name='create'),
    path('list/', views.ListCustomerView.as_view(), name='list'),
    path('get/<str:TC>/', views.CustomerDetailView.as_view(), name='get'),
    path('delete/<str:TC>/', views.CustomerDeleteView.as_view(), name='delete'),
]
