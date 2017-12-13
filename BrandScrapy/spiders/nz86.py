import scrapy
from BrandScrapy.items import NZ86Item

class NZ86Spider(scrapy.Spider):
    name = 'nz86'
    allowed_domains = ['www.nz86.com']

    def start_requests(self):
        url = 'http://www.nz86.com/brands/p'
        for index in range(1,303):
            yield scrapy.Request(url=url+str(index)+'/', callback=self.parse_list)

    def parse_list(self, response):
        for url in response.xpath('//div[@class="ppdq_list"]/ul/li/div[1]/div[@class="list_c"]/div/span/a/@href').extract():
            # item = NZ86Item()
            #
            # item['url'] = url
            #
            # yield item
            yield scrapy.Request(url=url, callback=self.parse_brand)

    def parse_brand(self, response):
        item = NZ86Item()

        zh_name = response.xpath('//div[@class="name-wrap"]/b/text()').extract_first()

        if zh_name is None:
            zh_name = response.xpath('//div[@class="brd-name-box"]/b/text()').extract_first()
            en_name = response.xpath('//p[@class="brd-name-eng"]/text()').extract_first()

            if en_name is None:
                item['name'] = zh_name
            else:
                item['name'] = zh_name + en_name.replace("\n", "").replace("\r", "").replace("\t", "")

        else:
            en_name = response.xpath('//div[@class="name-wrap"]/span/text()').extract_first()

            if en_name is None:
                item['name'] = zh_name
            else:
                item['name'] = zh_name + en_name.replace("\n", "").replace("\r", "").replace("\t", "")

        item['url'] = response.url
        item['style'] = response.xpath('//ul[@class="brd-file"]/li[1]/div').xpath('string(.)') \
            .extract_first().replace("\n", "").replace("\r", "").replace("\t", "")
        item['position'] = response.xpath('//ul[@class="brd-file"]/li[2]/div').xpath('string(.)') \
            .extract_first().replace("\n", "").replace("\r", "").replace("\t", "")
        item['age'] = response.xpath('//ul[@class="brd-file"]/li[3]/div').xpath('string(.)') \
            .extract_first().replace("\n", "").replace("\r", "").replace("\t", "")

        yield item

