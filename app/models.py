"""
Definition of models.
"""

from django.db import models
from django.contrib import admin
from datetime import datetime
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class Article(models.Model):

    author = models.ForeignKey(User, null=True, blank=True, on_delete = models.SET_NULL, verbose_name = "Автор")
    header = models.CharField(max_length=70, unique_for_date = 'date', verbose_name = "Заголовок")
    description = models.TextField(max_length=300, verbose_name = "Описание")
    content = models.TextField(max_length=3000, verbose_name = "Содержание")
    date = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = "Опубликована")
    image = models.FileField(default = 'temp.jpg', verbose_name = "Путь к картинке")

    def get_absolute_url(self):
        return reverse("article", args=[str(self.id)])

    def __str__(self):
        return self.header

    class Meta:
        ordering = ["-date"]
        verbose_name = "статья блога"
        verbose_name_plural = "статьи блога"

class Comment(models.Model):

    text = models.TextField(max_length=300, verbose_name = "Текст")
    date = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = "Опубликован")
    author = models.ForeignKey(User, null=True, blank=True, on_delete = models.SET_NULL, verbose_name = "Автор")
    post = models.ForeignKey(Article, on_delete = models.CASCADE, verbose_name = "Статья")

    def get_absolute_url(self):
        return reverse("comment", args=[str(self.id)])

    def __str__(self):
        a = 31 if len(self.text) > 30 else len(self.text)
        return self.text[:a]

    class Meta:
        ordering = ["-date"]
        verbose_name = "комментарий"
        verbose_name_plural = "комментарии"

admin.site.register(Article)
admin.site.register(Comment)


