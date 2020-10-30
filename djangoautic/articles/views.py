from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View
from django.utils.decorators import method_decorator
from .models import Article, Comment
from . import forms


# Create your views here.

class ArticlesList(View):

    template_name = 'article/articles_list.html'

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all().order_by('date')
        return render(request, 'articles/articles_list.html',
                      {'articles': articles})


class ArticlesDetailsView(View):

    template_name = 'article/articles_detail'

    def get(self, request, slug):
        request.session['last_visited_slug'] = slug
        article = Article.objects.get(slug=slug)
        comments = Comment.objects.filter(related_article=slug)
        form = forms.CreateComment()
        return render(request, 'articles/article_detail.html',
                      {'article': article, 'comments': comments, 'form': form})


class ArticleCreationView(View):

    template_name = 'article/articles_create.html'

    def get(self, request):
        form = forms.CreateArticle()
        return render(request, 'articles/article_create.html', {'form': form})

    @method_decorator(login_required)
    def post(self, request):
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')


class CreateCommentView(View):

    # @login_required(login_url="/accounts/login/")
    def post(self, request):
        slug = request.session['last_visited_slug']
        if request.method == 'POST':
            form = forms.CreateComment(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.author = request.user
                instance.related_article = slug
                instance.save()
                return redirect('articles:detail', slug=slug)

            form = forms.CreateComment()
