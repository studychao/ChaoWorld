# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.syndication.views import Feed

from .models import Post

class AllPostsRssFeed(Feed):

    title = "超的博客"

    link ="/"

    description = "超超的私人空间哦"

    def items(self):
        return Post.objects.all()

    def item_title(self,item):
        return '[%s] %s' % (item.category,item.title)

    def item_description(self,item):
        return item.body
