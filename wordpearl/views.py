from django.http import JsonResponse
from .models import Pearl, Oyster
from .serializers import PearlSerializer, OystersSerializer
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

@api_view(['GET', 'POST', 'DELETE'])
def oystersList(request):
    if request.method == 'GET':
        oysters = Oyster.objects.all()
        serializer = OystersSerializer(oysters, many=True)
        return JsonResponse({'oysters': serializer.data}, safe=False)