from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from . import forms

# Create your views here.


def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/articles_list.html',
                  {'articles': articles})


def article_detail(request, slug):
    request.session['last_visited_slug'] = slug
    article = Article.objects.get(slug=slug)
    comments = Comment.objects.filter(related_article=slug)
    form = forms.CreateComment()
    return render(request, 'articles/article_detail.html',
                  {'article': article, 'comments': comments, 'form': form})


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
    return render(request, 'articles/article_create.html', {'form': form})
<<<<<<< HEAD


=======


>>>>>>> Comments_functional
@login_required(login_url="/accounts/login/")
def create_comment(request):
    slug = request.session['last_visited_slug']
    if request.method == 'POST':
        form = forms.CreateComment(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.related_article = slug
            instance.save()
<<<<<<< HEAD
            return redirect('articles:list')
    else:
        form = forms.CreateComment()
    return render(request, 'articles/article_create.html', {'form': form})
=======
            return redirect('articles:detail', slug=slug)

        form = forms.CreateComment()
>>>>>>> Comments_functional
