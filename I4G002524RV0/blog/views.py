from turtle import update
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import (
    DeleteView,
    CreateView,
    UpdateView,
)
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Post

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = "post_list.html"


class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    template_name = "post_form.html"
    success_url = "/"


class PostDetailView(DetailView):
    model = Post
    fields = "__all__"
    template_name = "post_details.html"


class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    template_name: "post_form.html"
    success_url = reverse_lazy("blog:all")


class PostDeleteView(DeleteView):
    model = Post
    field = "__all__"
    template_name: "post_confirm_delete.html"
    success_url = reverse_lazy("blog:all")
