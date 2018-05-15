import markdown

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render,get_object_or_404
from .models import Post,Category,Tag
from comments.forms import CommentForm
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request,'index.html')

def me(request):
    return render(request,'me.html')

def updateplan(request):
    return render(request,'updateplan.html')

def blog(request):
    post_list = Post.objects.all().order_by('-created_time')
    paginator = Paginator(post_list,5)
    
    page = request.GET.get('page')
    
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request,'blog.html',context={'post_list':posts})

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    post.increase_views()
    
    md = markdown.Markdown(extensions=['markdown.extensions.extra','markdown.extensions.codehilite','markdown.extensions.toc',])
    post.body = md.convert(post.body)
    post.toc = md.toc
    form = CommentForm()
    comment_list =post.comment_set.all()
    
    context = {'post':post,'form':form,'comment_list':comment_list}

    return render(request, 'detail.html', context=context)

def archives(request,year,month):
    post_list = Post.objects.filter(created_time__year=year,created_time__month=month).order_by('-created_time')
    paginator = Paginator(post_list,5)
    
    page = request.GET.get('page')
    
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request,'blog.html',context={'post_list':posts})

def category(request,pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    paginator = Paginator(post_list,5)
    
    page = request.GET.get('page')
    
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request,'blog.html',context={'post_list':posts})

def tag(request,pk):
    tag = get_object_or_404(Tag, pk=pk)
    post_list = Post.objects.filter(tags=tag).order_by('-created_time')
    paginator = Paginator(post_list,5)
    
    page = request.GET.get('page')
    
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request,'blog.html',context={'post_list':posts})

def search(request):
    q = request.GET.get('q')
    error_msg = ''

    if not q:
        error_msg = "Don't leave it blank"
        return render(request,'blog.html',{'error_msg':error_msg})

    post_list = Post.objects.filter(Q(title__icontains=q) | Q(body__icontains=q))

    return render(request,'blog.html',{'error_msg':error_msg,'post_list':post_list})
