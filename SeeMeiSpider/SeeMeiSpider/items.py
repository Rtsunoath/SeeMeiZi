# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy_djangoitem import DjangoItem
from index.models import Feeds


class SeemeispiderItem(DjangoItem):
    django_model = Feeds
