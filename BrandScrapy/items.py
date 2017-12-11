# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BrandscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class RayliItem(scrapy.Item):
    name = scrapy.Field()
    creator = scrapy.Field()
    create_time = scrapy.Field()
    source_place = scrapy.Field()
    attach = scrapy.Field()
