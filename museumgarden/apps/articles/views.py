from django.shortcuts import render
from .models import Article, Author
from django.conf import settings
import os
def Show_articles(request):
    articles = Article.objects.all()
    articles_author = Article.author.through.objects.all()
    author = Author.objects.all()
    context = {
        'articles': articles,
        'articles_author': articles_author,
        "authors": author,
    }
    return render(request, 'article_app/blog.html', context)


def Show_detail_articles(request, slug):
    article = Article.objects.get(slug=slug)
    images_list = os.listdir(settings.MEDIA_ROOT+f"images/articles/article-{article.id}")
    article.view_number += 1
    article.save()
    articles_author = Article.author.through.objects.all()
    authors = Author.objects.all()
    context = {
        "article": article,
        "articles_author": articles_author,
        "authors": authors,
        "images_list": images_list,
    }
    return render(request, "article_app/showDetails.html", context)

