from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from EmployeeApp.models import Departments,Employees
from EmployeeApp.serializers import DepartmentSerializer,EmployeeSerializer
from django.http.response import JsonResponse
from django.core.files.storage import default_storage
from django.http import HttpResponse
# Create your views here.

@csrf_exempt
def departmentApi(request,id=0):
    if request.method=='GET':
        departments=Departments.objects.all()
        department_serializer=DepartmentSerializer(departments,many=True)
        return JsonResponse(department_serializer.data,safe=False)
    elif request.method=='POST':
        department_data=JSONParser().parse(request)
        department_serializer=DepartmentSerializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("added successfully!",safe=False)
        return JsonResponse("failed to add",safe=False)
    elif request.method=='PUT':
        department_data=JSONParser().parse(request)
        department_id = department_data.get('DepartmentId')
        department = Departments.objects.get(DepartmentId=department_id)
        department_serializer=DepartmentSerializer(department,data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("update successfull",safe=False)
        return JsonResponse("update failed",safe=False)
    elif request.method=='DELETE':
        department=Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("delete success",safe=False)
        
        
@csrf_exempt
def employeeApi(request,id=0):
    if request.method=='GET':
        employees=Employees.objects.all()
        employee_serializer=EmployeeSerializer(employees,many=True)
        return JsonResponse(employee_serializer.data,safe=False)
    elif request.method=='POST':
        employee_data=JSONParser().parse(request)
        employee_serializer=EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("added successfully!",safe=False)
        return JsonResponse("failed to add",safe=False)
    elif request.method=='PUT':
        employee_data=JSONParser().parse(request)
        employee_id = employee_data.get('EmployeeId')
        employee = Employees.objects.get(EmployeeId=employee_id)
        employee_serializer=EmployeeSerializer(employee,data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("update successfull",safe=False)
        return JsonResponse("update failed",safe=False)
    elif request.method=='DELETE':
        employee=Employees.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("delete success",safe=False)
        
@csrf_exempt
def SaveFile(request):
    file=request.FILES['uploadedFile']
    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)

def index(request):
    return HttpResponse("Welcome to the EmployeeApp!")
    
        

