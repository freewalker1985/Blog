import markdown

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DeleteView
from django.db.models import Q
from .models import Article, Category, Tag


class CommonView(ListView):
    """
    公共类
    """
    model = Article
    context_object_name = 'article_list'
    template_name = 'myblog/list.html'
    paginate_by = 2
    allow_empty = True


class IndexView(CommonView):
    pass


class ArticleListView(CommonView):
    """
    list类
    """

    def get_queryset(self):
        queryset = super(ArticleListView, self).get_queryset()
        queryset = queryset.filter(status='published')
        return queryset


class ArticleDetailView(DeleteView):
    """
    detail类
    """
    model = Article
    template_name = 'myblog/detail.html'
    context_object_name = 'article_detail'

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(Article, pk=kwargs['pk'])
        obj.views += 1
        obj.save(update_fields=['views'])
        return super(ArticleDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        article = super(ArticleDetailView, self).get_object(queryset=None)
        article.content = markdown.markdown(article.content,
                                            extensions=[
                                                'markdown.extensions.extra',
                                                'markdown.extensions.codehilite',
                                                'markdown.extensions.toc',
                                            ])
        return article


# def CategoryView(request, pk=None):
#     category = get_object_or_404(Category, pk=pk)
#     article_list = category.article_set.all()
#     return render(request, 'myblog/list.html', {'article_list': article_list})


class CategoryView(ListView):
    """
    category视图类
    """
    model = Article
    template_name = 'myblog/list.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        category = get_object_or_404(Category, pk=self.kwargs['pk'])
        return super(CategoryView, self).get_queryset().filter(category__name=category.name, status='published')


class TagView(CommonView):
    """
    Tag视图类
    """
    # model = Article
    model = 'Tag'
    template_name = 'myblog/list.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        tag = get_object_or_404(Tag, pk=self.kwargs['pk'])
        return tag.article_set.all()
        # return super(TagView, self).get_queryset().filter(tag__name__iexact=tag.name)


def search(request):
    q = request.GET.get('q')
    error_msg = ''
    if not q:
        error_msg = "请输入关键字"
        return render(request, 'myblog/list.html', {'error_msg': error_msg})
    artlice_list = Article.objects.filter(Q(title__icontains=q) | Q(content__icontains=q))
    return render(request, 'myblog/list.html', {'error_msg': error_msg, 'article_list': artlice_list})
