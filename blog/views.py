from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

# Create your views here.
def index(request):
    post = Post.objects.order_by('-created_date')
    # data =  { 'mydata' : 'I miei dati'}
    return render(request, 'blog/index.html', { 'posts' : post})

def detail(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'blog/detail.html', { 'post' : post} )