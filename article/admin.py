# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

#导入
from models import Article #from article.models import Artilce
# Register your models here.

admin.site.register(Article)