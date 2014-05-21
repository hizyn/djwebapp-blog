#coding=utf-8
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(u'文章分类', max_length=64)

    class Meta:
        ordering = ['-id']

    def __unicode__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(u'标题', max_length=128)
    author = models.ForeignKey(User)
    content = models.TextField(u"内容")
    pub_data = models.DateTimeField(auto_now_add=True)
    po_type = models.ForeignKey(Category, verbose_name=u'文章分类', blank=True, null=True)

    class Meta:
        ordering = ['-id']

    def __unicode__(self):
        return self.title
