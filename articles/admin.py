from django.contrib import admin
from articles.models import Article, Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
        list_display = ('name', 'email', 'body', 'post', 'created', 'active')
        list_filter = ('created', 'active', 'updated')
        search_fields = ('name', 'email', 'body')

@admin.action(description="Mark selected article as published")
@admin.action(description="Mark selected article as drafted")
def make_update_description(queryset):
         queryset.update(status="published")


def make_drafted_description(queryset):
    queryset.update(status="draft")


class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "status"]
    ordering = ["title"]
    actions = [
        make_update_description,
        make_drafted_description,
    ]
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Article, ArticleAdmin)