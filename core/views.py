from django.shortcuts import render
from core.models import Post

# Create your views here.
def blog_view(request):
  posts = Post.objects.all()
  return render(request, 'public/blog.html', { 'posts': posts })
