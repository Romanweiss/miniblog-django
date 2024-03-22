from tkinter import CASCADE
from django.db import models
from django.forms import CharField


class Post(models.Model):
    """Данные о записи/посте"""

    title = models.CharField(
        "Заголовок записи",
        max_length=100,
    )
    description = models.TextField(
        "Текст записи",
    )
    author = models.CharField(
        "Имя автора",
        max_length=100,
    )
    date = models.DateField("Дата публикации")

    # Пути к изображениям - %Y - указание года
    img = models.ImageField("Изображение", upload_to="image/%Y")

    def __str__(self):
        return f"{self.title}, {self.author}"

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"


class Comments(models.Model):
    """Комментарий"""

    email = models.EmailField()
    name = models.CharField("Имя", max_length=50)
    text_comments = models.TextField("Текст комментария", max_length=2000)
    post = models.ForeignKey(
        to=Post, verbose_name="Публикация", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.name}, {self.post}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

class Likes(models.Model):
    '''Лайки'''
    ip = models.CharField('IP-адрес', max_length=50)
    pos = models.ForeignKey(to=Post, on_delete=models.CASCADE, verbose_name='Публикация')

    