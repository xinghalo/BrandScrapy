import scrapy
import requests
from BrandScrapy.items import ChinassppItem

class proxy2(scrapy.Spider):
    name = 'chinasspp'
    allowed_domains = ['www.chinasspp.com']
    start_urls = ['http://www.chinasspp.com/brand/']

    def parse(self, response):
        for category_url in response.xpath('//p[@class="title_1"]/a/@href').extract():
            for i in range(1,1000):
                yield scrapy.Request(url=category_url+str(i)+'/', callback=self.parse_category)


    def parse_category(self, response):
        for brand_url in response.xpath('//p[@class="first"]/a/@href').extract():
            yield scrapy.Request(url=brand_url, callback=self.parse_brand)

    def parse_brand(self, response):

        item = ChinassppItem()

        item['name'] = response.xpath('//div[@class="l_info"]/strong/text()').extract_first()
        item['url'] = response.url
        item['sim'] = response.xpath('//div[@class="l_brands"]/ul/li/a/text()').extract()
        #item['story'] = response.xpath('//div[@class="r r_about"]').xpath('string(.)').extract()
        item['category'] = response.xpath('//div[@class="l_info"]/ul[@class="link"]/li[2]/text()').extract_first()

        yield item