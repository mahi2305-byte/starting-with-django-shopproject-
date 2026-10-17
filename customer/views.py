from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Customer
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def get_customers(request):
    customer = Customer.objects.all().values()
    return Response(list(customer))