from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views.generic import *
from blog.models import *


class IndexListView(ListView):
    context_object_name = "list"

    def get_context_data(self, **kwargs):
        context = super(IndexListView, self).get_context_data(**kwargs)


class ArticleListView(ListView):
    model = Article

# class CategoryDetail(ListView):
#     model = Article


def article_list(request):

    return HttpResponse("")


def article_create(request):
    return HttpResponse("")


def article_detail(request):
    return HttpResponse("")


def article_edit(request):
    return HttpResponse("")


def article_delete(request):
    return HttpResponse("")