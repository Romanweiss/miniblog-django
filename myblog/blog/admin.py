from django.contrib import admin
from .models import Post, Comments


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author"]
    list_display_links = ["title", "author"]


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ["name", "post"]
    list_display_links = ["name", "post"]
