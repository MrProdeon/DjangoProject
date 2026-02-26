from django.shortcuts import render
from django.urls import reverse_lazy
from blog.models import BlogEntry
from django.views.generic import ListView, DetailView, TemplateView, DeleteView
from django.views.generic.edit import CreateView, UpdateView

# Create your views here.

class BlogCreateView(CreateView):

    model = BlogEntry
    fields = ["name", "content", "preview", "is_publicated"]
    template_name = "blog_create_view.html"
    success_url = reverse_lazy("blogs:home")

class BlogListView(ListView):
    model = BlogEntry
    template_name = "home.html"
    context_object_name = "posts"

    def get_queryset(self):

        return BlogEntry.objects.filter(is_publicated=True)


class BlogDetailView(DetailView):
    model = BlogEntry
    template_name = "blog_detail.html"
    context_object_name = "post"

    def get_object(self, queryset=None):

        obj = super().get_object()
        obj.views_count += 1
        obj.save()

        return obj

class BlogUpdateView(UpdateView):
    model = BlogEntry
    fields = ["name", "content", "preview", "is_publicated"]
    template_name = "blog_create_view.html"
    success_url = reverse_lazy("blogs:home")

class BlogDeleteView(DeleteView):
    model = BlogEntry
    template_name = "blog_confirm_delete.html"


