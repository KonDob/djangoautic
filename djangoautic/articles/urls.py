from django.urls import re_path
from django.conf.urls import include, url
from . import views

app_name = 'articles'

urlpatterns = [
    re_path(r'^$', views.article_list, name="list"),
    re_path(r'^create/$', views.article_create, name="create"),
    re_path(r'^/create_comment/$', views.create_comment,
            name='create_comment'),
    re_path(r'^(?P<slug>[\w]+)/$', views.article_detail, name='detail'),
]