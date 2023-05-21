from django.shortcuts import render, redirect
from .models import Post
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import AddPostForm, EditForm
from django.urls import reverse_lazy



# Create your views here.
def index(request):
    posts = Post.objects.all()
    ordering = ['date_created']
    return render(request, 'index.html', {'posts': posts, 'ordering':ordering})



def post(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'post.html', {'post': post})



class AddPostView(CreateView):
    model = Post
    form_class = AddPostForm
    template_name = 'add_post.html'


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    fields = ['title', 'title_tag', 'body']



class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('index')
