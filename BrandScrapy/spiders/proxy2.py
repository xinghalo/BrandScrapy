import scrapy
import requests
from BrandScrapy.items import Proxy2Item

class proxy2(scrapy.Spider):
    name = 'proxy2'
    allowed_domains = ['www.data5u.com']
    start_urls = ['http://www.data5u.com/']

    def parse(self, response):
        for ul in response.xpath('//ul[@class="l2"]'):

            ip = ul.xpath('./span[1]/li/text()').extract_first()
            port = ul.xpath('./span[2]/li/text()').extract_first()
            http = ul.xpath('./span[4]/li/a/text()').extract_first()

            # try:
            #     result = requests.get('http://httpbin.org/ip', proxies={ http : ip+':'+port}, timeout=3)
            #
            #     # http://httpbin.org/ip
            #     if result.status_code == 200 and result.json()['origin'] != '223.100.142.112':
            #         item = Proxy2Item()
            #         item['url'] = http + '://' + ip + ':' + port
            #         print(item['url'])
            #         yield item
            #
            # except Exception as err:
            #
            #     print("超时")

            item = Proxy2Item()
            item['url'] = http + '://' + ip + ':' + port
            print(item['url'])
            yield item






