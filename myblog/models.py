from django.db import models
from django.urls import reverse

import markdown


class Article(models.Model):
    """
    博客文章
    """
    STATUS_CHOICES = (
        ('draf', 'Draf'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=50, verbose_name="标题")
    desc = models.CharField(max_length=50, blank=True,
                            null=True, verbose_name="描述")
    category = models.ForeignKey(
        'Category', blank=True, null=True, verbose_name="分类")
    tag = models.ManyToManyField(
        'Tag', blank=True, null=True, verbose_name="标签")
    content = models.TextField(verbose_name="文章内容")
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, verbose_name="文章状态")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")
    modify_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")
    views = models.PositiveIntegerField(default=0, verbose_name="浏览量")
    likes = models.PositiveIntegerField(default=0, verbose_name="点赞数")

    class Meta:
        verbose_name = verbose_name_plural = '博客文章'
        ordering = ['-create_time']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})


class Category(models.Model):
    """
    分类
    """
    name = models.CharField(max_length=10, verbose_name="分类名称")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")
    modify_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta:
        verbose_name = verbose_name_plural = '文章分类'

    def __str__(self):
        return self.name


class Tag(models.Model):
    """
    标签
    """
    name = models.CharField(max_length=10, verbose_name="分类名称")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")
    modify_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta:
        verbose_name = verbose_name_plural = '文章标签'

    def __str__(self):
        return self.name
