from django.conf.urls import url
from .views import ArticleListView, ArticleDetailView, CategoryView, TagView, search

urlpatterns = [
    url(r'^$', ArticleListView.as_view(), name='list'),
    url(r'^detail/(?P<pk>\d+)/$', ArticleDetailView.as_view(), name='detail'),
    url(r'^category/(?P<pk>\d+)/$', CategoryView.as_view(), name='category'),
    # url(r'^category/(?P<pk>\d+)/$', CategoryView, name='category'),
    url(r'^tag/(?P<pk>\d+)/$', TagView.as_view(), name='tag'),
]