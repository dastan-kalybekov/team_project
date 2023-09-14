from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

RATINGS = (
    (1, 'Очень плохо'),
    (2, 'Плохо'),
    (3, 'Так себе'),
    (4, 'Хорошо'),
    (5, 'Отлично'),

)


class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title


class Rating(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATINGS)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'

    def __str__(self):
        return f"{self.post.id} {self.user.username} {self.rating}"


class Comment(models.Model):
    text = models.CharField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Комментария'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        try:
            return self.text[:20] + '...'
        except Exception:
            return self.text
