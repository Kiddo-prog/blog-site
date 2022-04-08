from django.contrib import admin

from article_api.models import Post, AuthorProfile

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "slug", "status"]
    ordering = ["title"]
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
admin.site.register(AuthorProfile)