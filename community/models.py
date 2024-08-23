from django.db import models
from django.conf import settings
from posts.models import Post
from auths.models import MutsaUser

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    comment_writer = models.ForeignKey(MutsaUser, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.nickname} - {self.text[:20]}'

class Like(models.Model):
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    like_writer = models.ForeignKey(MutsaUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.nickname} liked {self.post.title}'
