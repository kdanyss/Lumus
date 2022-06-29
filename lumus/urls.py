from django.urls import path
from .views import Inicio, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CommentCreateView, CommentDeleteView, CategoryCreateView, CategoryListView, CategoryDetailView, CategoryDeleteView
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', Inicio.as_view(), name='Inicio'),
    path('navegacao/', PostListView.as_view(), name='navegacao'),
    path('profile/listcategory/', CategoryListView.as_view(), name='category-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('post/<int:pk>/comment', CommentCreateView.as_view(), name='comment-create'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('profile/newcategory/', CategoryCreateView.as_view(), name='category-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
    path('post/<int:pk>/commentdelete/', CommentDeleteView.as_view(), name='comment-delete'),


]
