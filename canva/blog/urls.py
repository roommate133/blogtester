from django.urls import path
from . import views

app_name='blog'


urlpatterns = [
    path("blog/",views.blog,name="blog"),
    path("blog_detail",views.blog_detail,name="blog-detail"),
    path("article-form/",views.add_article,name="article-form"),
    path("edit-article/<int:id",views.article_edit,name="edit-article"),
    path("example/",views.example,name="example"),
]
