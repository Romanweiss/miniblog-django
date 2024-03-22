from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostView.as_view(), ),
    path('<int:pk>/', views.PostDetail.as_view(), ),
    path('review/<int:pk>', views.AddComments.as_view(), name='add_comments'),
    path('<int:pk>/add-likes/', views.AddLike.as_view(), name='add_likes'),
    path('<int:pk>/del-likes/', views.DelLike.as_view(), name='del_likes'),
]
