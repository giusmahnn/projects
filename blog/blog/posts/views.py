from django.shortcuts import render, redirect
from .models import Post
from django.views.generic import CreateView, UpdateView
from .forms import AddPostForm

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})



def post(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'post.html', {'post': post})



class AddPostView(CreateView):
    model = Post
    form_class = AddPostForm
    template_name = 'add_post.html'
    #fields = '__all__'


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ['title', 'title_tag', 'body']