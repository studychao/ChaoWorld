from django.db import models

class usercomment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    text = models.TextField()
    reply = models.TextField(blank=True)
    created_time = models.DateTimeField(auto_now_add=True)


