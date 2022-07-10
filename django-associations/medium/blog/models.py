from django.db import models

# Create your models here.
class User(models.Model):
    pass


class Post(models.Model):
    # post.user
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name="posts") # user.posts


class Comment(models.Model):
    # comment.user
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments") # user.comments
    
    # comment.post
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments") # post.comments







