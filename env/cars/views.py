from django.http import JsonResponse
from .models import cars
from .serializers import carserializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'PUT', 'DELETE'])
def cars_detail(request, id):
    try:
        cars = cars.object.get(pic=id)
    except cars.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = carserializer(cars)
        return Response(serializer.data)
    elif request.method == 'POST':
        pass
    elif request.method == 'DELETE':
        pass
    



@api_view(['GET', 'POST'])
def cars_list(request):
    if request.method == 'GET':
        serializer = carserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        


def cars_list(request):
    cars = cars.objects.all()
    serializer = carserializer(cars, many=True)
    return JsonResponse(serializer.data, safe=False)

    