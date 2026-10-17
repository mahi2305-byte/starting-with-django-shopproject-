from . import views
from django.urls import path

urlpatterns = [
    path('customers/', views.get_customers, name='get_customers')
]
