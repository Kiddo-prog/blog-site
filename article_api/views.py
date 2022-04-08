from rest_framework import generics
from article_api.models import Post, AuthorProfile
from .serializers import PostSerializer, AuthorSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class AuthorList(generics.ListCreateAPIView):
    queryset = AuthorProfile.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetail(generics.RetrieveDestroyAPIView):
    queryset = AuthorProfile.objects.all()
    serializer_class = AuthorSerializer