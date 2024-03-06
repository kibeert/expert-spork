from django.shortcuts import render, get_object_or_404
from .models import Article
from django.contrib.auth.decorators import login_required

# Create your views here.

def article_view(request, *args, **kwargs):
    articles = Article.objects.all().order_by('date_published')
    return render(request, "base/Articles.html", {'articles': articles})

def dynamicpage(request, *args, **kwargs):
    data = Article.objects.all()
    return render(request, 'base/dynamic.html')

def article_detail(request,article_id,  *args, **kwargs):
    article = get_object_or_404(Article, pk = article_id)
    return render(request, 'base/article_detail.html', {'article':article})

@login_required(login_url="/accounts/login/")
def article_create(request, *args, **kwargs):
    return render(request, 'base/articlecreate.html')