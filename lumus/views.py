from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post



def Inicio(request):
    return render(request, 'Index.html')



class PostListView(ListView):
    model = Post
    template_name = 'navegation.html'
    context_object_name = 'posts'

    def get_queryset(self):
        txt_title = self.request.GET.get('title')

        if txt_title:
            posts = Post.objects.filter(title__icontains=txt_title, status='Mostrar').order_by('-date_posted')
        else:
            posts = Post.objects.filter(status='Mostrar').order_by('-date_posted')
        return posts