# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from models import *

def index(request):
    articles = Article.objects.all()
    # return HttpResponse(content=b"hello world!") #返回一个字符串
    return render(request, "index.html", locals())

def detail(request, id):
    article = Article.objects.get(id=id)
    return render(request, "detail.html", locals())

def search_tag(request, tag):
    article_list = Article.objects.filter(category=tag)
    return render(request, "category.html", {'article_list':article_list})





