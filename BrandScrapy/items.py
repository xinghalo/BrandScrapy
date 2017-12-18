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

class ChinassppItem(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    sim = scrapy.Field()
    story = scrapy.Field()
    category = scrapy.Field()

class Proxy2Item(scrapy.Item):
    url = scrapy.Field()

class ProxyItem(scrapy.Item):
    url = scrapy.Field()
    proxy = scrapy.Field()

class NZ86Item(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    style = scrapy.Field()
    position = scrapy.Field()
    age = scrapy.Field()


class NaefuItem(scrapy.Item):
    # 品牌名称
    name = scrapy.Field()
    # 适用年龄
    age = scrapy.Field()
    # 品牌故事
    story = scrapy.Field()
    # url
    url = scrapy.Field()

    def csv(self):
        arr = [self['name'],
               self['age'],
               #self['story'],
               self['url']]

        return ",".join(arr)+"\n"

class RayliItem(scrapy.Item):
    # 品牌中文名（英文名）
    name = scrapy.Field()
    # 创建者
    creator = scrapy.Field()
    # 创建时间
    create_time = scrapy.Field()
    # 发源地
    source_place = scrapy.Field()
    # 归属集团
    attach = scrapy.Field()
    # 品牌故事
    #story = scrapy.Field()
    # 目录
    category= scrapy.Field()
    # 功能
    function = scrapy.Field()
    # 系列
    series = scrapy.Field()
    # 网址
    url = scrapy.Field()

    def csv(self):
        arr = [self['name'],
               self['creator'],
               self['create_time'],
               self['source_place'],
               self['attach'],
               self['url'],
               self['category'],
               self['function'],
               self['series'],
               ]

        return ",".join(arr)+"\n"