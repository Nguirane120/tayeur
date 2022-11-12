from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.http import HttpResponse

from ..models import Employee
from ..serializers import EmployeeSerializer

class EmployeeList(APIView):

    def get(self, request, format=None):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)

        return Response(serializer.data, status=200)
        
class CreateEmployee(generics.CreateAPIView):
    queryset = Employee.objects.all
    serializer_class = EmployeeSerializer

    def post(self, request, format=None):
        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

class DetailEmployee(APIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self,pk, request, format=None):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)

        return Response(serializer.data, status=200)

    def put(self, pk, request, format=None):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=200)

        return Response(serializer.errors, status=400)

    def delete(self, pk, request, format=None):
        employee = self.get_object(pk)
        employee.delete()

        return Response(status=200)


