from .models import GetPostImage, PostImage, Post, Comment
from rest_framework import serializers

class GetPostImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GetPostImage
        fields = ('url', 'title', 'image_url')

class PostImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PostImage
        fields = ('url', 'title', 'image')

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('url', 'title', 'description')

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('url', 'comment', 'related_post')
