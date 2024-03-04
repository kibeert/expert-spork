from django.shortcuts import render
from .models import Article

# Create your views here.

def article_view(request, *args, **kwargs):
    articles = Article.objects.all().order_by('date_published')
    return render(request, "base/Articles.html", {'articles': articles})