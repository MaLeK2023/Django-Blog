from django.shortcuts import render , redirect
from .models import Post 
from .form import PostForm 
from django.views import generic

# Create your views here.


class PostList(generic.ListView): # html post_list , context object_list post_list
    model = Post

class PostDetail(generic.DetailView): # html post_detail , context object post
    model = Post


class PostCreate(generic.CreateView):
    model = Post
    fields = ['title','content','image','tags']
    success_url = '/blog/'


class PostEdit(generic.UpdateView):
    model = Post
    fields = ['title','content','image','tags']
    success_url = '/blog/'
    template_name = 'posts/edit.html'


class PostDelete(generic.DeleteView):
    model = Post
    success_url = '/blog/'

