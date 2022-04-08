from unicodedata import name
from django.urls import path

from .views import PostList, PostDetail, AuthorList, AuthorDetail

# from blog.article_api.views import PostList

app_name = "article_api"

urlpatterns = [
    path("", PostList.as_view(), name="post-detail"),
    path("<int:pk>", PostDetail.as_view(), name="post-list"),
    path("profile/", AuthorList.as_view(), name="author-list"),
    path("profile/<int:pk>/", AuthorDetail.as_view(), name="author-detail"),
]
