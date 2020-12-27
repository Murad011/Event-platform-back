from django.urls import path
from .views import (EventAPIView,event_detail)
from rest_framework_simplejwt import views as jwt_views
from .views import LogoutAPIView, LoginAPIView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('eventapi/', EventAPIView.as_view()),
    path('eventdetail/<int:id>/',event_detail),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]