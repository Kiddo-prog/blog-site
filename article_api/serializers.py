from rest_framework import serializers
from .models import Post, AuthorProfile


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # title author date_created text status slug active
        fieldset = (
            None,
            (
                "id",
                "title",
                "author",
                "date_created",
                "description",
                "text",
                "status",
            ),
        ), (("profile"), ("username", "image", "about"))
        fields = (
            "id",
            "title",
            "author",
            "date_created",
            "description",
            "text",
            "status",
        )


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorProfile
        fields = ("id", "username", "image", "about")
