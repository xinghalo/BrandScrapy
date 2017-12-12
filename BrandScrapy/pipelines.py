# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs

class BrandscrapyPipeline(object):

    def __init__(self):
        self.file = codecs.open('rayli.csv', 'wb', encoding='utf-8')

    def process_item(self, item, spider):

        # line = item['name']+","+item['creator']+","+item['create_time']+","+item['source_place']+\
        #        ","+item['attach']+","+item['category']+","+item['gongneng']+","+item['xilie']+","+item['url']+"\n"

        # line = item['name'] + "," + item['creator'] + "," + item['create_time'] + "," + item['source_place'] + \
        #        "," + item['attach'] + "," + item['url'] + "\n"

        #line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(item.csv())
        return item

    def spider_closed(self, spider):
        self.file.close()