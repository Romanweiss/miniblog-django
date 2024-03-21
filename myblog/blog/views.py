from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Post
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
        return redirect(f'/{pk}')
