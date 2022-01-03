from django.contrib.auth import get_user_model
from django.db import models


class Article(models.Model):
    header = models.CharField(max_length=150)
    body = models.TextField()

    parent_article = models.ForeignKey("self", on_delete=models.PROTECT, blank=True, null=True)

    is_deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    is_edited = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    article = models.ForeignKey(Article, on_delete=models.PROTECT)
