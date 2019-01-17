from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone



# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by('published_date')#filter(published_date__lte = timezone.now()).order_by('published_date')
    return render(request, 'myblog/post_list.html', {'posts':posts})

def post_detail(request, id):
    get_id = get_object_or_404(Post, id=id)
    #get_id = Post.objects.all()
    return render(request, 'myblog/post_detail.html', {'get_id':get_id})



