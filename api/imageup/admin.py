from django.contrib import admin
from .models import GetPostImage, PostImage

@admin.register(GetPostImage)
class Post(admin.ModelAdmin):
    pass

@admin.register(PostImage)
class Post(admin.ModelAdmin):
    pass

