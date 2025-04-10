from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Question(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def get_absolute_url(self):
        return reverse("questions:question_detail", kwargs={"slug": self.slug})
    
    def __str__(self):
        return self.title
    
    