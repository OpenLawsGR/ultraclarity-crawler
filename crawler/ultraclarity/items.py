# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class UltraclarityItem(scrapy.Item):
    # Define the fields for your item here like:
    title = scrapy.Field()
    url = scrapy.Field()
    desc = scrapy.Field()
    pass
