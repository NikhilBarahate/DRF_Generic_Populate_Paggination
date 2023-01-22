from django.shortcuts import render
from app1.models import Employee
from app1.serializers import EmployeeSerializer
from rest_framework import generics
from app1.pagination import MyPagination, MyPagination1, MyPagination2


# Create your views here.
class EmployeeApiViews(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = MyPagination2
    