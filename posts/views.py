from django.shortcuts import render, get_object_or_404,redirect
from django.contrib import messages
# Create your views here.
from .models import Post,Author
from .forms import PostModelForm

def posts_list(request):
    all_posts = Post.objects.all()
    context={
        'all_posts':all_posts
    }
    messages.info(request,"Here are the list of Blog Posts")
    return render(request,'posts/posts_list.html',context)

def post_detail(request,slug):
    unique_post=get_object_or_404(Post,slug=slug)
    context = {
        'post': unique_post
    }
    messages.info(request,"Here is the  single Blog Post")
    return render(request,'posts/posts_detail.html',context)

def post_create(request):
    author,created = Author.objects.get_or_create(
        user=request.user,
        email=request.user.email,
        mobile="1234567890"
    )

    form =PostModelForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.instance.author=author
        form.save()
        messages.info(request,"Successfully created the Blog Post")
        return redirect("/posts/")
    context={
        'form': form
    }
    return render(request,'posts/posts_create.html',context)


def post_update(request,slug):
    unique_post=get_object_or_404(Post,slug=slug)
    context = {
        'post': unique_post
    }
    form =PostModelForm(request.POST or None,request.FILES or None,instance=unique_post)
    if form.is_valid():
        form.instance.author=unique_post.author
        form.save()
        messages.info(request,"Successfully updated the Blog Post")
        return redirect("/posts/")
    context ={
        'form': form
    }
    return render(request,'posts/posts_create.html',context)


def post_delete(request,slug):
    unique_post=get_object_or_404(Post,slug=slug)
    unique_post.delete()
    messages.info(request,"Successfully deleted the Blog Post")
    return redirect("/posts/")