
# -*- coding: utf-8 -*-
from mptt.models import MPTTModel, TreeForeignKey
from mptt.managers import TreeManager
from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class Article(models.Model):
	pub_date = models.DateField()
	title = models.CharField(max_length=200)
	content = models.TextField()
	class Meta:
		verbose_name='Статья'
		verbose_name_plural='Статьи'
	def __str__(self):
		return self.title










class ArticleManager(TreeManager):
	def let(self):
		queryset = self.get_descendants().filter(level__lte=3)
		return queryset
	def viewable(self):
		queryset = self.get_queryset().filter(level__lte=2)
		return queryset




class Comment(MPTTModel):
	objects = ArticleManager()
	article = models.ForeignKey('Article', on_delete=models.CASCADE,
								related_name='comment')
	created_date = models.DateTimeField(default=timezone.now)
	name = models.CharField(max_length=50, unique=True)
	parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
	user = models.CharField(default='anonim', max_length=32)
	text = models.TextField(default='нет текста')

	class MPTTMeta:
		order_insertion_by = ['created_date']

	class Meta:
		verbose_name='Комментарий'
		verbose_name_plural='Комментарии'

	def __str__(self):
		return self.name

