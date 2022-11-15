from django.http import JsonResponse
from .models import Pearl
from .serializers import PearlSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def pearlList(request):
    if request.method == 'GET':
        pearls = Pearl.objects.all()
        serializer = PearlSerializer(pearls, many=True)
        return JsonResponse({'pearls': serializer.data}, safe=False)
    if request.method == 'POST':
        serializer = PearlSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def getPearlById(request, id):
    try:
        pearl = Pearl.objects.get(pk=id)
    except Pearl.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = PearlSerializer(pearl, many=False)
        return JsonResponse({'pearl': serializer.data}, safe=False)
    elif request.method == 'PUT':
        serializer = PearlSerializer(pearl, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        pearl.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
