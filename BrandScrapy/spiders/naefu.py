import scrapy
from BrandScrapy.items import NaefuItem

class RayliSpider(scrapy.Spider):
    name = 'naefu'
    allowed_domains = ['na.efu.com.cn',
                       'brand.efu.com.cn']

    def start_requests(self):
        url = 'http://na.efu.com.cn/brand/na/list-'
        for index in range(1,22):
            yield scrapy.Request(url=url+str(index)+'.html', callback=self.parse)

    def parse(self, response):
        for u in response.xpath('//div[@class="photo-lst"]/ol/li/div/div[2]/div/a/@href').extract():
            yield scrapy.Request(url=u, callback=self.parse_brand)

    def parse_brand(self, response):

        item = NaefuItem()

        item['name'] = response.xpath('//div[@class="conaH2"]/a/text()').extract_first().strip()
        item['story'] = response.xpath('//div[@class="blk17 mtop10"]/div[2]').xpath('string(.)').extract_first().strip()
        item['age'] = response.xpath('//div[@id="zsdiv"]/ul/li[1]/span[@class="sp-b"]/text()').extract_first()
        item['url'] = response.url

        yield item