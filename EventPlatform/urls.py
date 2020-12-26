from django.urls import path
from .views import (EventAPIView,event_detail)

urlpatterns = [
    path('eventapi/', EventAPIView.as_view()),
    path('eventdetail/<int:id>/',event_detail)
    
]