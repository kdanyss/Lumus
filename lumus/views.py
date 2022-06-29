from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category, Post, Comment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User


class Inicio(ListView):
    model = User
    template_name = 'Index.html'
    context_object_name = 'users'



#----POSTS----
class PostListView(ListView):
    model = Post
    template_name = 'navegation.html'
    context_object_name = 'posts'

    def get_queryset(self):
        # obtendo variável de pesquisa. 
        txt_title = self.request.GET.get('title')

        if txt_title:
            posts = Post.objects.filter(title__icontains=txt_title, status='Mostrar').order_by('-date_posted')
        else:
            posts = Post.objects.filter(status='Mostrar').order_by('-date_posted')
        return posts


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post

    # a função detalha apenas se o objeto tiver status: Mostrar, caso contrário, erro.
    def get_queryset(self):
        posts = Post.objects.filter(status='Mostrar')
        return posts

    # a função está pegando os comentários de acordo o 'post.id' para o DetailView do Post
    def get_context_data(self, **kwargs):
        # obtendo o contexto da nossa superclasse.
        context = super().get_context_data(**kwargs)
        self.post = get_object_or_404(Post, id=self.kwargs['pk'])
        # adicionando novas informações de contexto no queryset. 
        context['comment_list'] = Comment.objects.filter(post= self.post, status='Mostrar')
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'category', 'image', 'status']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


#usuário criador e Moderator podem editar postagem
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'category', 'image', 'status']
    success_url = "/navegacao/"

    def form_valid(self, form):
        #form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author or self.request.user.profile.moderator == 'Moderator':
            return True
        return False


#usuário criador e Moderator podem deletar o post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/navegacao/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author or self.request.user.profile.moderator == 'Moderator':
            return True
        return False



#----COMMENTS----
class CommentCreateView(LoginRequiredMixin, CreateView):

    model = Comment
    fields = ['content', 'image']
    success_url = "/navegacao/"

    def form_valid(self, form):
        form.instance.post = Post.objects.get(pk=self.kwargs.get('pk'))
        form.instance.author = self.request.user
        return super().form_valid(form)


#usuário criador e Moderator podem deletar comentário
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    success_url = "/navegacao/"
    
    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author or self.request.user.profile.moderator == 'Moderator':
            return True
        return False   



#----MODERATOR ADD's----
class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categorys'

    def get_queryset(self):
        cats = Category.objects.all()
        print(cats)
        return cats


class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Category

    # a função está pegando os posts de acordo o 'category.id' para o DetailView do Category
    def get_context_data(self, **kwargs):
        # obtendo o contexto da nossa superclasse.
        context = super().get_context_data(**kwargs)
        self.category = get_object_or_404(Category, id=self.kwargs['pk'])
        # obtendo variável de pesquisa. 
        txt = self.request.GET.get('title')
        # Adicionando as novas informações de retorno de contexto. 
        if txt:
            context['post_list'] = Post.objects.filter(title__icontains=txt, category= self.category, status='Mostrar')
        else:
            context['post_list'] = Post.objects.filter(category= self.category, status='Mostrar')
        return context


class CategoryCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Category
    fields = ['title']
    success_url = "/navegacao/"

    # acesso apenas por Moderators, senão, retona forbidden 403(improvável, apenas uma restrição a + por garantia).
    def test_func(self):
        return self.request.user.profile.moderator == 'Moderator'

    def form_valid(self, form):
        return super().form_valid(form)

    # verifica quem está fazendo a requisição, outro a mais.
    def test_func(self):
        if self.request.user.profile.moderator == 'Moderator':
            return True
        return False


class CategoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Category
    success_url = "/profile/listcategory/"

    def test_func(self):
        return self.request.user.profile.moderator == 'Moderator'    

    def test_func(self):
        post = self.get_object()
        if self.request.user.profile.moderator == 'Moderator':
            return True
        return False