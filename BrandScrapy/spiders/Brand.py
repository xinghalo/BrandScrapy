# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import scrapy
from BrandScrapy.items import RayliItem

class BrandSpider(scrapy.Spider):
    name = 'Brand'
    allowed_domains = ['hzp.rayli.com.cn']
    #start_urls = ['http://hzp.rayli.com.cn/brand.html/']
    def start_requests(self):
        yield scrapy.Request(url='http://hzp.rayli.com.cn/brand.html/', callback=self.parse_index)


    def parse_index(self, response):
        for brand in response.xpath('//div[@class="ghy_w1180 g_zmgb1"]/div[@class="g_zmpic mt20"]'):
            for sub_li in brand.xpath('./ul[1]/li'):
                # item = RayliItem()
                # item['name'] = sub_li.xpath(
                #     './div[@class="g_zmpic_01_wz1"]/span[@class="g_ys2"]/a/text()').extract_first().decode("utf-8")
                page_url  = sub_li.xpath(
                    './div[@class="g_zmpic_01_wz1"]/span[@class="g_ys2"]/a/@href').extract_first().decode("utf-8")
                # item['en_name'] = sub_li.xpath(
                #     './div[@class="g_zmpic_01_wz1"]/span[@class="g_ys4"]/a/text()').extract_first().decode("utf-8")

                yield scrapy.Request(url='http://hzp.rayli.com.cn'+page_url, callback=self.parse_brand)

                # yield item

            for sub_hidden_li in brand.xpath('./ul[2]/li'):
                # item = RayliItem()
                # item['name'] = sub_hidden_li.xpath(
                #     './span[@class="g_ys2"]/a/text()').extract_first().decode("utf-8")
                page_url = sub_hidden_li.xpath(
                    './span[@class="g_ys2"]/a/@href').extract_first().decode("utf-8")
                # item['en_name'] = sub_hidden_li.xpath(
                #     './span[@class="g_ys4"]/a/text()').extract_first().decode("utf-8")
                yield scrapy.Request(url='http://hzp.rayli.com.cn' + page_url, callback=self.parse_brand)


    def parse_brand(self, response):
        item = RayliItem()

        item['name'] = response.xpath(
            '//div[@class="left hzpk_ys3  hzpk_mbx2"]/text()').extract_first().decode("utf-8")
        item['creator'] = response.xpath(
            '//div[@class="hzpk_dpcent_qh2_n1"]/dl[1]/text()').extract_first().decode("utf-8")
        item['create_time'] = response.xpath(
            '//div[@class="hzpk_dpcent_qh2_n1"]/dl[2]/text()').extract_first().decode("utf-8")
        item['source_place'] = response.xpath(
            '//div[@class="hzpk_dpcent_qh2_n1"]/dl[3]/text()').extract_first().decode("utf-8")
        item['attach'] = response.xpath(
            '//div[@class="hzpk_dpcent_qh2_n1"]/dl[4]/text()').extract_first().decode("utf-8")

        yield item
