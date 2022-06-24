from django.urls import path
from .views import (
    PostCreateView,
    PostDeleteView,
    PostDetailView,
    PostListView,
    PostUpdateView,
)

# from .views import PostCreateView

app_name = "blog"

urlpatterns = [
    path("", PostListView.as_view(), name="all"),
    path("create/", PostCreateView.as_view(), name="post_create"),
    path("delete/<slug:slug>/", PostDeleteView.as_view(), name="post_delete"),
    path("update/<slug:slug>/", PostUpdateView.as_view(), name="post_update"),
    path("read/<slug:slug>/", PostDetailView.as_view(), name="post_detail"),
]
