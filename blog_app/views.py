from django.shortcuts import render
from django.shortcuts import render ,get_object_or_404
from django.views import generic
from django.utils import timezone
from blog_app.models import Post

# Create your views here.
class ListView(generic.ListView):
    template_name = 'blog_app/post_list.html'
    context_object_name = 'list_post'

    def get_queryset(self):
        return Post.objects.all()


class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog_app/detail.html'

    def get_queryset(self):
        return Post.objects
