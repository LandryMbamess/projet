from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Categorie(models.Model):
	nom = models.CharField(max_length = 40, unique=True)

	def __str__(self):
		return self.nom


class Article(models.Model):

	STATUT_ARTCILE = (('brouillon','brouillon'),('publier','publier'))

	auteur = models.ForeignKey(User, on_delete = models.CASCADE)
	categorie = models.ForeignKey(Categorie, on_delete = models.CASCADE)
	titre = models.CharField(max_length = 100)
	contenu = models.TextField(null = True)
	statut = models.CharField(max_length = 10, choices = STATUT_ARTCILE, default = 'brouillon')
	date = models.DateTimeField(auto_now_add= True, verbose_name = "datepub")

	def __str__(self):
		return self.titre

class Commentaire(models.Model):
	auteur = models.ForeignKey(User, on_delete = models.CASCADE)
	article = models.ForeignKey(Article, on_delete = models.CASCADE)
	contenu = models.CharField(max_length = 150)
	date = models.DateTimeField(auto_now_add= True)

	def __str__(self):
		return self.contenu
