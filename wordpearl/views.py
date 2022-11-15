from django.http import JsonResponse
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#pearlList
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

#pearlsById
@api_view(['GET', 'PUT', 'DELETE'])
def getPearlById(request, id):
    try:
        pearl = Pearl.objects.get(pk=id)
    except Pearl.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = PearlSerializer(pearl, many=False)
        return Response({'pearl': serializer.data})
    elif request.method == 'PUT':
        serializer = PearlSerializer(pearl, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        pearl.delete()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

#oysterList
@api_view(['GET', 'POST'])
def oystersList(request):
    if request.method == 'GET':
        oysters = Oyster.objects.all()
        serializer = OystersSerializer(oysters, many=True)
        return JsonResponse({'oysters': serializer.data}, safe=False)
    if request.method == 'POST':
        serializer = OystersSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

#oystersByID
@api_view(['GET', 'DELETE'])
def oysterList(request, id):
    try:
      oyster = Oyster.objects.get(pk=id)
    except Oyster.DoesNotExist:
      return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = OystersSerializer(oyster)
        return Response({'oyster': serializer.data})
    elif request.method == 'DELETE':
        oyster.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#comments
@api_view(['GET', 'POST'])
def commentList(request):
        if request.method == 'GET':
            comments = Comment.objects.all()
            serializer = CommentSerializer(comments, many=True)
            return JsonResponse({'comments': serializer.data}, safe=False)
        if request.method == 'POST':
            serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

#commentsByID
@api_view(['GET', 'PUT', 'DELETE'])
def comment(request, id):
    try:
        comment = Comment.objects.get(pk=id)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
