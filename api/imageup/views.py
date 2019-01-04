from django.shortcuts import render
from .models import GetPostImage, PostImage
from rest_framework import viewsets
from .serializers import GetPostImageSerializer, PostImageSerializer

class GetPostImageViewSet(viewsets.ModelViewSet):
    queryset = GetPostImage.objects.all()
    serializer_class = GetPostImageSerializer

class PostImageViewSet(viewsets.ModelViewSet):
    queryset = PostImage.objects.all()
    serializer_class = PostImageSerializer
    print("Call: PostViewSet")

