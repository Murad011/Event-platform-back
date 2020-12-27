from django.urls import path, include
from .views import (EventAPIView,event_detail)
from django.contrib.auth.models import User
from rest_framework import routers
from .views import UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)



urlpatterns = [
    path('eventapi/', EventAPIView.as_view()),
    path('eventdetail/<int:id>/',event_detail),
    path('api/', include(router.urls)),
    
]