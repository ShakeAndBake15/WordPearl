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
