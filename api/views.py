from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import CompanySerializer
from tracker.models import Company

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET': '/api/companies'},
        {'GET': '/api/companies/id'},
        {'GET': '/api/companies/id/employee'},
    ]

    return Response(routes)


@api_view(['GET'])
def getCompanies(request):
    company = Company.objects.all()
    serializer = CompanySerializer(company, many = True)

    return Response(serializer.data)


@api_view(['GET'])
def getCompany(request,pk):
    company = Company.objects.get(id = pk)
    serializer = CompanySerializer(company, many = False)

    return Response(serializer.data)