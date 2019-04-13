from django import forms
from django.contrib.auth.models import User
from .models import Article,Categorie,Commentaire


class ArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = ('titre', 'categorie', 'contenu', 'statut')

	def publier(self):
		self.statut ='publier'

class comForm(forms.ModelForm):
	class Meta:
		model = Commentaire
		fields = ('contenu',)

class categorieForm(forms.ModelForm):
	class Meta:
		model = Categorie
		fields = '__all__'

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username','password','email')
