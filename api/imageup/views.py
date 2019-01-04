from django.shortcuts import render
from .models import GetPostImage, PostImage, Post, Comment
from rest_framework import viewsets
from .serializers import GetPostImageSerializer, PostImageSerializer, PostSerializer, CommentSerializer

class GetPostImageViewSet(viewsets.ModelViewSet):
    queryset = GetPostImage.objects.all()
    serializer_class = GetPostImageSerializer

class PostImageViewSet(viewsets.ModelViewSet):
    queryset = PostImage.objects.all()
    serializer_class = PostImageSerializer
    print("Call: PostViewSet")

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
