from django.shortcuts import render

from.models import Post

# Create your views here.

def homepage(request):
    all_text = Post.objects.all()
    return render(request, 'posts/home.html', {
        'all_posts_list':all_text,
    })
