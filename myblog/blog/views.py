from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import JsonResponse

# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html',  context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-created_at']
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(title__icontains=query).order_by('-created_at')
        return Post.objects.all()

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-created_at')
    
class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author or self.request.user.is_staff:
            return True
        return False
    
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog-home')
    
def form_valid(self, form):
    form.instance.author = self.request.user
    messages.success(self.request, 'Post created successfully!')
    return super().form_valid(form)

def delete_multiple_posts(request):
    if request.method == 'POST':
        post_ids = request.POST.getlist('post_ids')
        posts = Post.objects.filter(id__in=post_ids, author=request.user)
        deleted_count = posts.count()
        posts.delete()
        return JsonResponse({'success': True, 'message': f'{deleted_count} bài viết đã được xóa.'})
    return JsonResponse({'success': False, 'message': 'Yêu cầu không hợp lệ.'})

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})