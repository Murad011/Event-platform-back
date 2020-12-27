from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import mixins
from .models import Event
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from .serializers import  EventSerializer
from django.http import HttpResponse, JsonResponse
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets



class EventAPIView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    def get(self, request):
        return self.list(request)
        
    def post(self, request):
        return self.create(request)



@api_view(['GET','DELETE'])
def event_detail(request,id):
    event = Event.objects.get(id=id)
    
    if request.method == 'GET':
        serializer = EventSerializer(event)
        return Response(serializer.data) 

    elif request.method == 'DELETE':
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



@api_view(['GET','DELETE'])
def user_detail(request,id):
    user = User.objects.get(id=id)
    
    if request.method == 'GET':
        serializer = UserSerializer(event)
        return Response(serializer.data) 

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)