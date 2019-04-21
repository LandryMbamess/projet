#from django.shortcuts import render,redirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse_lazy



#class home(TemplateView):
#	template_name = "blog/index.html"

#def blog(request):
#	articles = Article.objects.filter(statut='publier').order_by('-date')[:6]
#	return render(request, "blog/blog.html", locals())
class blog(ListView):
	model = Article
	template_name = 'blog/blog.html'
	context_object_name='articles'
	queryset = Article.objects.filter(statut='publier').order_by('-date')[:6]


def listing(request):
	articles = Article.objects.filter(statut='publier').order_by('titre')
	paginator = Paginator(articles, 4)
	page = request.GET.get('page')
	try:
		articles = paginator.page(page)
	except PageNotAnInteger:
		articles = paginator.page(1)
	except EmptyPage:
		articles = paginator.page(paginator.num_page)
	paginate = True
	return render(request, 'blog/listing.html', locals())


#def detailArticle(request, article_id):
#	article = get_object_or_404(Article, pk=article_id)
#	return render(request, "blog/detail.html", locals())
class detailArticle(DetailView):
	model=Article
	context_object_name='article'
	template_name='blog/detail.html'



@login_required(login_url = 'blog:login')
def newArticle(request):
	form = ArticleForm(request.POST or None)
	if form.is_valid():
		form = form.save(commit=False)
		form.auteur = request.user
		form.save()
		return redirect('blog:detailArticle', form.id)
	return render(request, "blog/new_article.html", locals())

class delArt(DeleteView):
	template_name = 'blog/delArt.html'
	context_object_name = 'article'
	model = Article
	success_url = reverse_lazy('blog:blog')

#@login_required(login_url = 'blog:login')
class editArticle(UpdateView):
	template_name = 'blog/new_article.html'
	model = Article
	form_class = ArticleForm
	success_url = reverse_lazy('blog:blog')

@login_required(login_url = 'blog:login')
def newCom(request, pk):
	forms = comForm(request.POST or None)
	if forms.is_valid():
		forms = forms.save(commit=False)
		forms.auteur = request.user
		forms.article = Article.objects.get(pk=pk)
		forms.save()
		return redirect('blog:detailArticle', pk)
	return render(request, "blog/detail.html", locals())

#@login_required(login_url = 'blog:login')
#def ajoutCat(request):
#	error = False
#	form = catCategorie(request.POST or None)
#	if form.is_valid():
#		nom = form.cleaned_data['nom']
#		cat = Categorie.objects.all()
#		for ele in cat:
#			if ele.nom == nom:
#				error = True
#		if error is False:
#			form.save()
#			return redirect('blog:newArticle')
#	return render(request, "blog/newCat.html", locals())
class ajoutCat(CreateView):
	template_name = 'blog/newCat.html'
	form_class = categorieForm
	model = Categorie
	success_url = reverse_lazy('home')


#class inscription(CreateView):
#	models = User
#	fields = ('username', 'email', 'password')
#	template_name = 'blog/inscription.html'

#def inscription(request):
#	error = False
#	form=UserForm(request.POST or None)
#	if form.is_valid():
#		username = form.cleaned_data['username']
#		password = form.cleaned_data['password']
#		user = authenticate(username=username, password=password)
#		if not user:
#			form.save()
#			return redirect('blog:login')
#		else:
#			error = True
#	return render(request, "blog/inscription.html", locals())
class inscription(CreateView):
	model = User
	template_name = 'blog/inscription.html'
	form_class = UserForm
	success_url = reverse_lazy('home')