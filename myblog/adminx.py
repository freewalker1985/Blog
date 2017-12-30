from .models import Article, Category, Tag

import xadmin
from xadmin import views


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = 'Blog后台管理系统'
    site_footer = '鬼知道这里写什么'
    menu_style = "accordion"


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)


class ArticleAdmin(object):
    list_display = ['title', 'category', 'tag', 'status', 'views']


xadmin.site.register(Article, ArticleAdmin)


class CategoryAdmin(object):
    list_display = ['name']


xadmin.site.register(Category, CategoryAdmin)


class TagAdmin(object):
    list_display = ['name']


xadmin.site.register(Tag, TagAdmin)