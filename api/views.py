import api
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .models import Employee
from .serializers import EmployeeSerializer

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    return Response('Api calling')


@api_view(['GET'])
def empList(request):
    empList=Employee.objects.all()
    serializer= EmployeeSerializer(empList,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def empDetail(request,pk):
    emp= Employee.objects.get(id=pk)
    serializer=EmployeeSerializer(emp,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def empCreate(request):
    serializer= EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def empUpdate(request, pk):
    emp = Employee.objects.get(id=pk)
    serializer=EmployeeSerializer(instance=emp,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def empDelete(request,pk):
    emp=Employee.objects.get(id=pk)
    emp.delete()
    return Response('Employee deleted successfully')