from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework_simplejwt.views import (
        TokenObtainPairView,
        TokenRefreshView,
    )

router_v1 = DefaultRouter()
router_v1.register(r'posts', PostViewSet, basename='posts')
router_v1.register(r'posts/(?P<id>\d+)/comments', CommentViewSet,
                basename='comments') 
router_v1.register(r'group', GroupViewSet, basename='group')                 
#router_v1.register(r'follow', FollowView, basename='follow')   

urlpatterns = [
        path('v1/', include(router_v1.urls)),
        path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
        path('v1/follow/', FollowView.as_view()),
    ]
