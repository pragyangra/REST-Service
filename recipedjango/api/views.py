from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import baseSerializer
from .models import base

#decorator to make sure view can access the django rest methods
@api_view(['GET', ])
def apiOverview(request):
    api_urls = {
        'Update':'/update/',
        'IPAddress':'/ipadd/<str:pk>/',
    }

    return Response(api_urls)

@api_view(['POST'])
def baseCreate(request):
	serializer = baseSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['GET'])
def baseLookup(request, pk):
	bases = base.objects.get(domainName=pk)
	serializer = baseSerializer(bases, many=False)
	return Response(serializer.data)
