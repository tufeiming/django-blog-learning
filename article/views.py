from django.shortcuts import render

from article.models import ArticlePost


def article_list(request):
    articles = ArticlePost.objects.all()
    context = {'articles': articles}
    return render(request, 'article/list.html', context)


def article_detail(request, article_id):
    article = ArticlePost.objects.get(id=article_id)
    context = {'article': article}
    return render(request, 'article/detail.html', context)
