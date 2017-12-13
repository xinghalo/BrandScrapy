# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import json

class BrandscrapyPipeline(object):

    def __init__(self):
        #file_name = 'ip.json'
        file_name = 'nz86-303.json'
        # file_name = 'ip2.json'
        self.file = codecs.open(file_name, 'wb', encoding='utf-8')

    def process_item(self, item, spider):

        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        # self.file.write(item.csv())
        return item

    def spider_closed(self, spider):
        self.file.close()
