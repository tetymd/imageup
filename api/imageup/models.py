from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    image_url = models.URLField(max_length=200, default="localhost:8000")

    def __str__(self):
        return self.title
