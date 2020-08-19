from rest_framework import viewsets, exceptions, generics, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_fields = ('group', )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

     
class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    
    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get("id"))
        return post.comments

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get("id"))
        serializer.save(author=self.request.user, post=post)


class FollowView(generics.ListCreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=user__username', '=following__username')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)       