from django.shortcuts import render
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from django.http import HttpResponse


# Create your views here.


def html_response(request):
    return render(request, 'myapp/template.html')


def text_response(request):
    return HttpResponse("Это текстовый ответ")


class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
