from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from api.models import SunExposure
from api.serializers import SunExposureSerializer
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def sunexposure_list(request):
    if request.method == 'GET':
        sunexposures = SunExposure.objects.all()

        garden_id = request.GET.get('title', None)
        if garden_id is not None:
            sunexposures = sunexposures.filter(garden_id__icontains=garden_id)

        sunexposures_serializer = SunExposureSerializer(sunexposures, many=True)
        return JsonResponse(sunexposures_serializer.data, safe=False)

    elif request.method == 'POST':
        sunexposure_data = JSONParser().parse(request)
        sunexposure_serializer = SunExposureSerializer(data=sunexposure_data)
        if sunexposure_serializer.is_valid():
            sunexposure_serializer.save()
            return JsonResponse(sunexposure_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(sunexposure_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        sunexposures = SunExposure.objects.all()

        garden_id = request.GET.get('title', None)
        if garden_id is not None:
            sunexposures = sunexposures.filter(garden_id__icontains=garden_id)

        count = sunexposures.delete()
        return JsonResponse({'message': '{} SunExposures were deleted successfully!'.format(count[0])}, status=status.HTTP_200_OK)

@api_view(['GET', 'DELETE'])
def sunexposure_detail(request, pk):
    try: 
        sunexposure = SunExposure.objects.get(pk=pk) 
    except SunExposure.DoesNotExist: 
        return JsonResponse({'message': 'The SunExposure does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        sunexposure_serializer = SunExposureSerializer(sunexposure)
        return JsonResponse(sunexposure_serializer.data)
    elif request.method == 'DELETE':
        sunexposure.delete()
        return JsonResponse({'message': 'SunExposure was deleted successfully!'}, status=status.HTTP_200_OK)