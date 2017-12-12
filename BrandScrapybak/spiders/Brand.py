# -*- coding: utf-8 -*-
import scrapy
from BrandScrapy.items import RayliItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle

class BrandSpider(CrawlSpider):
    name = 'Brand'
    allowed_domains = ['hzp.rayli.com.cn']
    start_urls = ['http://hzp.rayli.com.cn/brand.html']

    rules = [
        Rule(sle(allow=(u'/\w+/index.html')), callback='parse_brand')
    ]

    def parse_brand(self, response):

        item = RayliItem()

        # " > 阿迪达斯(Adidas)"
        origin_name = response.xpath('//div[@class="left hzpk_ys3  hzpk_mbx2"]/text()').extract_first()
        item['name'] = str(origin_name).strip(" > ")

        # "创始人：阿道夫·达斯勒"
        origin_creator = response.xpath('//div[@class="hzpk_dpcent_qh2_n1"]/dl[1]/text()').extract_first()
        item['creator'] = str(origin_creator).strip("创始人：")

        # "创建时间：1920"
        origin_create_time = response.xpath('//div[@class="hzpk_dpcent_qh2_n1"]/dl[2]/text()').extract_first()
        item['create_time'] = str(origin_create_time).strip("创建时间：")

        # "发源地：德国"
        origin_source_place = response.xpath('//div[@class="hzpk_dpcent_qh2_n1"]/dl[3]/text()').extract_first()
        item['source_place'] = str(origin_source_place).strip("发源地：")

        # "所属集团：阿迪达斯"
        origin_attach = response.xpath('//div[@class="hzpk_dpcent_qh2_n1"]/dl[4]/text()').extract_first()
        item['attach'] = str(origin_attach).strip("所属集团：")

        #item['story'] = response.xpath('//div[@class="fl dpp_dp_01_right"]/div[5]/p/text()').extract_first()
        item['category'] = ";".join(i.decode("utf-8") for i in response.xpath('//div[@class="dpp_dp_02"]/div[2]/ul[1]/li/a/text()').extract())
        item['gongneng'] = ";".join(i.decode("utf-8") for i in response.xpath('//div[@class="dpp_dp_02"]/div[2]/ul[2]/li/a/text()').extract())
        item['xilie'] = ";".join(i.decode("utf-8") for i in response.xpath('//div[@class="dpp_dp_02"]/div[2]/ul[3]/li/a/text()').extract())

        item['url'] = response.url
        yield item
