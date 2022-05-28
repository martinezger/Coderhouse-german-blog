from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from blog.models import BlogModel
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm



class BlogList(ListView):

    model = BlogModel
    template_name = "blog/blog_list.html"


class BlogDetail(DetailView):

    model = BlogModel
    template_name = "blog/blog_detail.html"


class BlogCreate(LoginRequiredMixin, CreateView):

    model = BlogModel
    success_url = reverse_lazy("blog_list")
    fields = ["titulo", "sub_titulo", "cuerpo", "autor"]


class BlogUpdate(LoginRequiredMixin, UpdateView):

    model = BlogModel
    success_url = reverse_lazy("blog_list")
    fields = ["titulo", "sub_titulo", "cuerpo", "autor"]


class BlogDelete(LoginRequiredMixin, DeleteView):

    model = BlogModel
    success_url = reverse_lazy("blog_list")


class BlogLogin(LoginView):
    template_name = 'blog/blog_login.html'
    next_page = reverse_lazy("blog_list")


class BlogLogout(LogoutView):
    template_name = 'blog/blog_logout.html'


    
class SignUpView(SuccessMessageMixin, CreateView):
  template_name = 'blog/blog_crear_cuenta_form.html'
  success_url = reverse_lazy('blog_login')
  form_class = UserCreationForm
  success_message = "Your profile was created successfully"