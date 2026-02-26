from django.shortcuts import render
from django.urls import reverse_lazy
from blog.models import BlogEntry
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView

# Create your views here.

class BlogCreateView(CreateView):

    model = BlogEntry
    fields = ["name", "content", "preview"]
    template_name = "blog_create_view.html"
    success_url = reverse_lazy("blog:home")

class BlogListView(ListView):
    model = BlogEntry
    template_name = "home.html"
    context_object_name = "posts"

class BlogUpdateView(UpdateView):
    model = BlogEntry
    fields = ["name", "content", "preview"]
    template_name = "blog_create_view.html"
    success_url = reverse_lazy("blog:home")


