from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Event



class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
