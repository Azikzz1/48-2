from django.shortcuts import render, HttpResponse, redirect
from .models import Post
from posts.forms import PostCreateForm


def about_me(request):
    if request.method == 'GET':
        return HttpResponse("I am a cool boy")
    else:
        pass


def about_my_friend(request):
    if request.method == 'GET':
        return render(request, 'about_my_friend.html')


def post_list_view(request):
    if request.method == 'GET':
        if request.method == 'GET':
            post = Post.objects.get(id=id)
            return render(request, 'posts/post_detail.html', {'post': post})


def post_create_view(request):
    if request.method == 'GET':
        form = PostCreateForm()
        return render(request, 'posts/post_create.html', {'form': form})
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, 'posts/post_create.html', {'form': form})
        elif form.is_valid():
            form.save()

            return redirect('/posts/')
