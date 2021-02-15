from django.urls import path
from . import views
from blog.views import PostListView,PostCreateView,UserPostListView,PostDeleteView,PostDetailView,PostUpdateView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/update',PostUpdateView.as_view(), name='post-update'),
    path('post/new/', PostCreateView.as_view(), name='create-post'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
     path('project/', views.project, name='blog-project'),

]
