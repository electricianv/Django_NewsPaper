
from django.shortcuts import render, get_object_or_404
from .models import Article


def news_list(request):
    articles = Article.objects.all().order_by('-date_pub')  # Сортировка по убыванию даты
    return render(request, 'news/news_list.html', {'articles': articles})

def article_detail(request, id):
    article = get_object_or_404(Article, pk=id)
    return render(request, 'news/article_detail.html', {'article': article})



