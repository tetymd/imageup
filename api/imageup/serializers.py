from .models import GetPostImage, PostImage
from rest_framework import serializers

class GetPostImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GetPostImage
        fields = ('url', 'title', 'image_url')

class PostImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PostImage
        fields = ('url', 'title', 'image')

