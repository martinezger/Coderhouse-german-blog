from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import BlogModel


class BlogList(ListView):

    model = BlogModel
    template_name = "blog/blog_list.html"


class BlogDetail(DetailView):

    model = BlogModel
    template_name = "blog/blog_detail.html"


class BlogCreate(CreateView):

    model = BlogModel
    success_url = reverse_lazy("blog_list")
    fields = ["titulo", "sub_titulo", "cuerpo", "autor"]


class BlogUpdate(UpdateView):

    model = BlogModel
    success_url = reverse_lazy("blog_list")
    fields = ["titulo", "sub_titulo", "cuerpo", "autor"]


class BlogDelete(DeleteView):

    model = BlogModel
    success_url = reverse_lazy("blog_list")