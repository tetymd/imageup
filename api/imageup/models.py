from django.db import models

class GetPostImage(models.Model):
    title = models.CharField(max_length=50)
    image_url = models.URLField(max_length=200, default="localhost:8000")

    def __str__(self):
        return self.title

class PostImage(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=128)

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.TextField(max_length=128, null=True)
    related_post = models.ForeignKey('Post', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.comment
