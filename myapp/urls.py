from django.urls import path
from .views import PostListView, PostDetailView, html_response, text_response

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('html/', html_response, name='html_response'),
    path('text/', text_response, name='text_response'),
    path("posts/create/", views.post_create_view, name='post_create_view'),
]
