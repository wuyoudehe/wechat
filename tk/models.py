# -*- coding: utf-8 -*-
from __future__ import unicode_literals
 
from django.db import models
 
 
'''class KeyWord(models.Model):
    keyword = models.CharField(
        '关键词', max_length=256, primary_key=True, help_text='用户发出的关键词')
    content = models.TextField(
        '内容', null=True, blank=True, help_text='回复给用户的内容')
 
    pub_date = models.DateTimeField('发表时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)
    published = models.BooleanField('发布状态', default=True)
 
    def __unicode__(self):
        return self.keyword
 
    class Meta:
        verbose_name='关键词'
        verbose_name_plural=verbose_name'''
