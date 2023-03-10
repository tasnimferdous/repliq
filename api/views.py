from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import CompanySerializer
from tracker.models import Company,User


# API routes
@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET': '/api/companies'},
        {'GET': '/api/companies/id'},
        {'GET': '/api/companies/id/employee'},
    ]

    return Response(routes)


# Companes and their Informations
@api_view(['GET'])
def getCompanies(request):
    company = Company.objects.all()
    serializer = CompanySerializer(company, many = True)

    return Response(serializer.data)


# Single company info
@api_view(['GET'])
def getCompany(request,pk):
    company = Company.objects.get(id = pk)
    serializer = CompanySerializer(company, many = False)

    return Response(serializer.data)


# Add Employee to a particular company
@api_view(['POST'])
def addEmployee(request,pk):
    company = Company.objects.get(id = pk)
    data = request.data
    employee, created = User.objects.get_or_create(
        company = company,
        username = data['username'],
    )

    employee.designation = data['designation']
    employee.phone = data['phone']
    employee.address = data['address']
    employee.email = data['email']
    employee.password = data['password']

    employee.save()
    serializer = CompanySerializer(company, many = False)

    return Response(serializer.data)