from urllib import request
from django import views
from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Post, Likes
from .form import CommentsForm


class PostView(View):
    """Вывод записей"""

    def get(self, request):
        posts = Post.objects.all()
        return render(request, "blog/blog.html", {"post_list": posts})


class PostDetail(View):
    """Вывод отдельной страницы записи"""

    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        return render(request, "blog/blog-detail.html", {"post": post})


# class AddComments(View):
#     """Добавление комментариев"""

#     def post(self, request, pk):
#         form = CommentsForm(request.POST)
#         print(request.POST)
#         print(pk)
#         if form.is_valid():
#             form.save(commit=False)
#             form.post_id = pk
#             form.save()
#         return redirect('/')


class AddComments(View):
    """Добавление комментариев"""

    def post(self, request, pk):
        form = CommentsForm(request.POST)
        print(request.POST)
        print(pk)
        if form.is_valid():
            comment = form.save(commit=False)  # Создаем объект комментария
            comment.post_id = pk  # Устанавливаем post_id
            comment.save()  # Сохраняем комментарий
        return redirect(f"/{pk}")


def get_client_ip(request):
    """Получение ip-адреса"""
    x_get_forwarded = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_get_forwarded:
        ip = x_get_forwarded.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


class AddLike(View):
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            Likes.objects.get(ip=ip_client, pos_id=pk)
            return redirect(f"/{pk}")
        except:
            new_like = Likes()
            new_like.ip = ip_client
            new_like.pos_id = int(pk)
            new_like.save()
            return redirect(f"/{pk}")


class DelLike(View):
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            like = Likes.objects.get(ip=ip_client, pos_id=pk)
            like.delete()
            return redirect(f"/{pk}")
        except:
            return redirect(f"/{pk}")