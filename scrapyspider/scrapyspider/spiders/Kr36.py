import scrapy
from ..items import SpiderItem

class Kr36Spider(scrapy.Spider):
    name = 'KR36'
    allowed_domains = ['www.36kr.com']
    start_urls = ['http://www.36kr.com/']

    def parse(self, response):
        items = [] 
        lists= response.xpath('//div[@class="kr-home-flow-item"]')
        print(lists)
        for i in lists:
            item=SpiderItem()
            item['description']=i.xpath('div/div/div[2]/div[2]/p/a/text()').get()
            print(item['description'])
            items.append(item)
        return items   