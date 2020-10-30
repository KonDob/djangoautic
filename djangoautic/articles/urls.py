from django.urls import re_path
from django.conf.urls import include, url
from . import views

app_name = 'articles'

urlpatterns = [
    re_path(r'^$', views.ArticlesList.as_view(), name="list"),
    re_path(r'^create/$', views.ArticleCreationView.as_view(), name="create"),
    re_path(r'^create_comment/$', views.CreateCommentView.as_view(),
            name='create_comment'),
    re_path(r'^(?P<slug>[\w]+)/$', views.ArticlesDetailsView.as_view(),
            name='detail'),
]
