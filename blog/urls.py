from django.conf.urls import url
from blog.views import *

urlpatterns = [
    url(r'^$', IndexListView.as_view()),
    # url(r'^$', "blog.views.article_list"),
    # url(r'^create/$', "blog.views.article_create"),
    # url(r'^detail/$', "blog.views.article_detail"),
    # url(r'^edit/$', "blog.views.article_edit"),
    # url(r'^delete/$', "blog.views.article_delete"),
]