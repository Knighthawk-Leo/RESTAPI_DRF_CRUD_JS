from django.shortcuts import render , HttpResponse
from django.http import JsonResponse
# Create your views here.
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET' , 'POST'])
def employeeListView(request):
    if request.method=='GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer = EmployeeSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])       
def  employeeDetailView(request, pk):
    try:
        employee =Employee.objects.get(pk=pk)
        # return JsonResponse("Employee" + str(pk), safe=False)
    except Employee.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data )

    elif request.method == 'DELETE':
        employee.delete()
        return HttpResponse(status= 204)
    
    elif request.method == 'PUT':
        serializer = EmployeeSerializer(employee , data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data )
        else:
            return Response(serializer.errors )

    

        
