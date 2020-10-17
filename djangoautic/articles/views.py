from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from . import forms

# Create your views here.

def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/articles_list.html', {'articles': articles})

def article_detail(request,slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html',{'article':article})

@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
       form = forms.CreateArticle() 
    
    return render(request, 'articles/article_create.html', {'form':form})

@login_required
def create_comment(request):
    if request.method == 'POST':
        form = forms.CreateComment(request.POST)
        if form.is_valid(data=request.POST):
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect(request, 'articles/article_detail.html', {'slug':slug})
    else:
       form = forms.CreateComment() 

    return redirect(request, 'articles/article_detail.html', {'form':form})

       
       
@login_required
def comments_list(request):
    comments_list = Comment.objects.all()
    return render(request, 'articles/articles_list.html', {'comments_list': comments_list})