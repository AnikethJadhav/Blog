from django.urls import path
from . import views

urlpatterns = [
  path("", views.index, name="index"),
  path("posts", views.posts, name="posts"),
  #  path("posts/<slug:slug>", views.post_detail, name="post-detail"),
  path("posts/<slug:slug>", views.PostDetailView.as_view(), name="post-detail"),
  path("postcomment", views.CommentView.as_view(), name="post-comment"),
  path("readlater", views.read_later, name="read-later")
  # path("readlater", views.ReadlaterView.as_view(),  name="read-later")
]