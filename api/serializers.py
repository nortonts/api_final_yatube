from rest_framework import serializers
from .models import *
from rest_framework.validators import UniqueTogetherValidator
from rest_framework import generics


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date', 'group')
        model = Post

class GroupSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, required=False)

    class Meta:
        fields = '__all__'
        model = Group

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    post = serializers.IntegerField(source='pk', required=False)

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        model = Comment

class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', 
                                        default=serializers.CurrentUserDefault(),
                                        read_only=True)
    following = serializers.SlugRelatedField(slug_field='username',
                                             queryset=User.objects.all())
    class Meta:
        fields = ('user', 'following')
        model = Follow
        validators = [UniqueTogetherValidator(queryset=Follow.objects.all(),
                                              fields=('user', 'following'))]