# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
    id = models.IntegerField(unique=True, editable=False, primary_key=True) #文章id
    title = models.CharField(max_length=100) #文章的标题
    category = models.CharField(max_length=50, blank=False) #文章分类
    date_time = models.DateTimeField(auto_now_add=True) #创建时间
    content = models.TextField(blank=True, null=True) #文章内容 blank=True表示可以为空；null=True，内容为空，则在数据库中设置为null

    def __unicode__(self): #后台显示的内容：默认显示一个对象，重写方法此处是一个标题
        return self.title
    class Meta: #文章排序
        ordering = ['-date_time'] #['-date_time']
