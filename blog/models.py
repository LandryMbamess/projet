from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.utils.six import python_2_unicode_compatible

from fluent_comments.moderation import moderate_model, comments_are_open, comments_are_moderated
from fluent_comments.models import get_comments_for_model, CommentsRelation
from django.urls import reverse


class Categorie(models.Model):
	nom = models.CharField(max_length = 40, unique=True)

	def __str__(self):
		return self.nom

@python_2_unicode_compatible
class Article(models.Model):

	STATUT_ARTCILE = (('brouillon','brouillon'),('publier','publier'))

	auteur = models.ForeignKey(User, on_delete = models.CASCADE)
	categorie = models.ForeignKey(Categorie, on_delete = models.CASCADE)
	titre = models.CharField(max_length = 100)
	contenu = models.TextField(null = True)
	statut = models.CharField(max_length = 10, choices = STATUT_ARTCILE, default = 'brouillon')
	date = models.DateTimeField(auto_now_add= True, verbose_name = "datepub")

	comments_set = CommentsRelation()

	class Meta:
		verbose_name = "Article"
		verbose_name_plural = "Articles"

	def __str__(self):
		return self.titre

	comments = property(get_comments_for_model)
	comments_are_open = property(comments_are_open)
	comments_are_moderated = property(comments_are_moderated)

	def get_absolute_url(self):
		return reverse('blog:detailArticle', kwargs={'pk': self.id})

moderate_model(
    Article,
    publication_date_field='date',
    enable_comments_field='statut'
)


class Commentaire(models.Model):
	auteur = models.ForeignKey(User, on_delete = models.CASCADE)
	article = models.ForeignKey(Article, on_delete = models.CASCADE)
	contenu = models.CharField(max_length = 150)
	date = models.DateTimeField(auto_now_add= True)

	def __str__(self):
		return self.contenu