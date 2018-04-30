# -*- coding: utf-8 -*-
from django.db import models
from django import forms

# Create your models here.

class News(models.Model):
    title = models.CharField('标题', max_length=128)
    pub_date = models.DateTimeField('发布日期')
    views = models.IntegerField('浏览次数', default=0)
    description = models.TextField('内容')
    image = models.ImageField('上传图片', upload_to='news', help_text="请上传 344*244 像素的图片")

    design = 'design'
    internet = 'internet'

    news_choices = (
        (design, '设计'),
        (internet, '互联网'),
    )
    news_category = models.CharField('文章分类', max_length=8, choices=news_choices, default=design)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.title

class Advisory(models.Model):
    name = models.CharField('名字', max_length=128)
    tel = models.CharField('联系电话', max_length=128)
    content = models.TextField('需求')

    def __unicode__(self):              # __unicode__ on Python 2
        return self.name

class Cases(models.Model):
    title = models.CharField('标题', max_length=128)
    title2 = models.CharField('副标题', max_length=128)
    image = models.ImageField('上传图片', upload_to='cases', help_text="案例列表图片,请上传 380*270 像素的图片")
    image2 = models.ImageField('上传图片', upload_to='cases', help_text="案例详情图片, 请上传宽为 1170 像素的图片, 此选项可以为空", null=True, blank=True)
    image3 = models.ImageField('上传图片', upload_to='cases', help_text="案例详情图片, 请上传宽为 1170 像素的图片, 此选项可以为空", null=True, blank=True)
    image4 = models.ImageField('上传图片', upload_to='cases', help_text="案例详情图片, 请上传宽为 1170 像素的图片, 此选项可以为空", null=True, blank=True)
    image5 = models.ImageField('上传图片', upload_to='cases', help_text="案例详情图片, 请上传宽为 1170 像素的图片, 此选项可以为空", null=True, blank=True)
    image6 = models.ImageField('上传图片', upload_to='cases', help_text="案例详情图片, 请上传宽为 1170 像素的图片, 此选项可以为空", null=True, blank=True)
    image7 = models.ImageField('上传图片', upload_to='cases', help_text="案例详情图片, 请上传宽为 1170 像素的图片, 此选项可以为空", null=True, blank=True)
    description1 = models.TextField('项目需求')
    description2 = models.TextField('解决方案')
    description3 = models.TextField('成绩影响')
    pub_date = models.DateTimeField('发布日期')
    description4 = models.CharField('服务内容', max_length=128)
    description5 = models.CharField('客户名称', max_length=128)
    description6 = models.CharField('网站链接', max_length=128)

    uiux = 'uiux'
    application = 'application'
    website_design = 'website_design'

    news_choices = (
        (uiux, 'UIUX'),
        (application, '应用程序'),
        (website_design, '网站设计'),
    )
    news_category = models.CharField('文章分类', max_length=14, choices=news_choices, default=uiux)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.title
