from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    group = models.ForeignKey('Group', models.SET_NULL, blank=True, 
                               null=True, related_name="posts")
    author = models.ForeignKey(User, on_delete=models.CASCADE, 
                               related_name="posts")


class Group(models.Model):
    title = models.CharField(max_length=200)
    

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, 
                               related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, 
                             related_name="comments")
    text = models.TextField()
    created = models.DateTimeField("Дата добавления", auto_now_add=True, 
                                   db_index=True)

class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, 
                             related_name='follower', null=True)
    following = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name='following', null=True)
    class Meta:
        unique_together = ('user', 'following')

       