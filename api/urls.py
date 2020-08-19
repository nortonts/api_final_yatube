from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework_simplejwt.views import (
        TokenObtainPairView,
        TokenRefreshView,
    )

router_v1 = DefaultRouter()
router_v1.register('follow', FollowView, basename='Follow')
router_v1.register('posts', PostViewSet, basename='Post')
router_v1.register(r'posts/(?P<id>\d+)/comments', CommentViewSet, basename='Comment')
router_v1.register('group', GroupView, basename='Group')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
