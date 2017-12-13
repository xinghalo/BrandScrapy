import scrapy
import os
import requests
from BrandScrapy.items import ProxyItem

class proxy(scrapy.Spider):
    name = 'proxy'
    allowed_domains = ['www.kuaidaili.com']

    def start_requests(self):
        url = 'http://www.kuaidaili.com/free/inha/'
        for index in range(1,1000):
            yield scrapy.Request(url=url+str(index)+'/', callback=self.parse_list)

    def parse_list(self, response):
        for tr in response.xpath('//div[@id="list"]/table/tbody/tr'):
            ip = tr.xpath('./td[1]/text()').extract_first()
            port = tr.xpath('./td[2]/text()').extract_first()
            proxy = ip+':'+port

            try:
                result = requests.get('http://httpbin.org/ip', proxies={'http': proxy}, timeout=1)

                # http://httpbin.org/ip
                if result.status_code == 200 and result.json()['origin'] != '223.100.142.112':
                    item = ProxyItem()

                    item['url'] = 'http'
                    item['proxy'] = proxy

                    print("success " + 'http://' + proxy)
                    yield item

            except Exception as err:
                try:
                    result = requests.get('http://httpbin.org/ip', proxies={'https': proxy}, timeout=1)

                    # http://httpbin.org/ip
                    if result.status_code == 200 and result.json()['origin'] != '223.100.142.112':
                        item = ProxyItem()

                        item['url'] = 'https'
                        item['proxy'] = proxy

                        print("success " + 'https://' + proxy)
                        yield item

                except Exception as err:
                    print("pass "+proxy)

