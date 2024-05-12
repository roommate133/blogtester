from django.shortcuts import render,redirect,get_object_or_404
from .models import Article,Author,Tag
from django.core.exceptions import PermissionDenied
from .forms import ArticleForm
from django.core.paginator import Paginator
def blog(request):
    author_username=request.GET.get("author")
    authors=Article.objects.all()
    articles=Article.objects.all()
    tags=Tag.objects.all()
    tag_title=request.GET.get("tag")
    page_number=int(request.GET.get('page',1))
    if author_username:
        articles=articles.filter(author__user__username=author_username)
    if tag_title:
        articles=articles.filter(tags__title=tag_title)
    paginator=Paginator(articles,3)
    page=paginator.page(page_number)
    articles=page.object_list
    return render(request,"blog.html",context={'articles':articles,'authors':authors,'tags':tags,'paginator':paginator,'page':page})



def blog_detail(request):
    article=Article.objects.all(id=id)  
    return render(request,"blog-detail.html",context={'article':article})


def add_article(request):
    if request.method=='POST':
        data=request.POST.copy()
        data['author']=request.user.author.id
        form=ArticleForm(data=data,files=request.FILES)
        if form.is_valid():
            form.save(request.user.author)
            return redirect('blog:blog')
    else:
        form=ArticleForm()
        return render(request,"article-form.html",{'form':form})
    
    

def article_edit(request,id):
    article=get_object_or_404(Article,id=id)
    if article.author.user != request.user:
        raise PermissionDenied()
    if request.method == "POST":
        data=request.POST.copy()
        data['author']=request.user.author.id
        form=ArticleForm(data=data,files=request.FILES,instance=article)
        if form.is_valid:
            form.save(request.user.author)
            return redirect('blog:add-article')
        return render(request,'article-form.html',{'form':form})
    else:
        form=Article(instance=article)
        return render(request,'article-form.html',{'form':form})
    

def delete_article(request):
    article=get_object_or_404(Article,id=id)
    if article.author.user !=request.user:
        raise PermissionDenied()
    article.delete()
    return redirect("blog:blog")

def example(request):
    return render(request,"example.html")