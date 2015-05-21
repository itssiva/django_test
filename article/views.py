from django.shortcuts import render_to_response

# Create your views here.
from django.http import HttpResponse
from article.models import Article

def articles(request):
	return render_to_response('articles.html',{'articles' : Article.objects.all()})

def article(request, article_id=1):
	return render_to_response('article.html',{'article' : Article.objects.get(id = article_id)})