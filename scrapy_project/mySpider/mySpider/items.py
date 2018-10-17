# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    positionName = scrapy.Field()
    positionLink = scrapy.Field()
    companyName = scrapy.Field()
    workLocation = scrapy.Field()
    salary = scrapy.Field()
    publishTime = scrapy.Field()
