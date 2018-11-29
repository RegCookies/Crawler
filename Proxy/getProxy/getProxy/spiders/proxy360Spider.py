# -*- coding: utf-8 -*-
import scrapy
from getProxy.items import GetproxyItem
class Proxy360spiderSpider(scrapy.Spider):
    name = 'proxy360Spider'
    allowed_domains = ['www.xicidaili.com']
    start_urls = []
    wds = ['nn','nt','wn','wt']
    pages = 20 
    for ptype in wds:
        for i in range(1,pages+1):
            start_urls.append('http://www.xicidaili.com/'+ptype + '/' + str(i) )
    def parse(self, response):
        selector = response.xpath('//tr[@class=""]|//tr[@class="odd"]')
        items = [] 
        for sub in selector:
            item = GetproxyItem() 
            item['ip'] = sub.xpath('//td[2]/text()').extract()[0]
            item['port'] = sub.xpath('//td[3]/text()').extract()[0] 
            item['ip_type'] = sub.xpath('//td[5]/text()').extract()[0] 
            if sub.xpath('//td[4]/a/text()'):
                item['location'] = sub.xpath('//td[4]/a/text()').extract()[0]
            else:
                item['location'] = sub.xpath('//td[4]/text()').extract()[0]
            item['protocal'] = sub.xpath('//td[6]/text()').extract( )[0] 
            item['source'] = 'xicidaili'
            items.append(item)
        return items          