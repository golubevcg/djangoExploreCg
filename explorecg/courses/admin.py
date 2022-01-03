from django.contrib import admin
from courses.models import Article, Comment


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = "id", "header", "created_at", "parent_article", "is_deleted"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = "id", "user", "created_at", "article", "is_deleted"
