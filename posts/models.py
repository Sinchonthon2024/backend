from django.db import models

class Post(models.Model):
    CATEGORY_CHOICES = [
        ('소셜링', '소셜링'),
        ('나눔', '나눔'),
    ]
    
    SOCIAL_DETAIL_CHOICES = [
        ('스터디', '스터디'),
        ('문화', '문화'),
        ('취미', '취미'),
        ('여행', '여행'),
        ('음식', '음식'),
    ]
    
    SHARE_DETAIL_CHOICES = [
        ('생활용품', '생활용품'),
        ('음식', '음식'),
        ('가구', '가구'),
    ]
    
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    detail = models.CharField(max_length=10, choices=SOCIAL_DETAIL_CHOICES + SHARE_DETAIL_CHOICES)
    title = models.CharField(max_length=100)
    text = models.TextField()
    limit = models.IntegerField()
    link = models.CharField(max_length=255, blank=True, null=True) 
    deadline = models.DateTimeField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
