from django.http import JsonResponse
from django.shortcuts import render

from MyApplication.serializers import EmployeesSerializer
from MyApplication.models import Employees


# Create your views here.
def employee_list(request):
    employees = Employees.objects.all()
    serializer = EmployeesSerializer(employees, many=True)
    return JsonResponse({'employees': serializer.data})