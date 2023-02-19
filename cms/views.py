from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView

from cms.models import Gallery, Post


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['gallery'] = Gallery.objects.filter(status=True).order_by('id')[:3]
        context['posts'] = Post.objects.filter(status=True).order_by('id')[:3]

        return context


class PostView(DetailView):
    template_name = 'post.html'
    model = Post


class PostListView(ListView):
    template_name = 'post-list.html'
    model = Post
