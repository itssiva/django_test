from django.shortcuts import render_to_response

# Create your views here.
from django.http import HttpResponse
from article.models import Article
from forms import ArticleForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf



def articles(request):
	language = 'en-us'
	session_language = 'en-us'
	if 'lang' in request.COOKIES:
		language = request.COOKIES['lang']
	if 'lang' in request.session:
		session_language = request.session['lang']

	return render_to_response('articles.html',
								{'articles' : Article.objects.all(),
								'language' : language,
								'session_language' :  session_language},)

def article(request, article_id=1):
	return render_to_response('article.html',{'article' : Article.objects.get(id = article_id)})


def language(request, language='en-us'):
	response = HttpResponse("Setting lanuage to %s" %language)
	response.set_cookie('lang', language)
	request.session['lang'] = language
	return response

def create(request):
	form = ArticleForm(request.POST)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect('/articles/all')
	args = {}
	args.update(csrf(request))
	args['form'] = form
	return render_to_response('create_article.html', args)


def like_article(request, article_id):
	if article_id:
		article = Article.objects.get(id = article_id)
		article.likes += 1
		article.save()
		return HttpResponseRedirect('/articles/get/%s'%article_id)

