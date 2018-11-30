# -*- coding: utf-8 -*-
import scrapy
from meiju100.items import Meiju100Item

class Meiju100spiderSpider(scrapy.Spider):
    name = 'meiju100Spider'
    allowed_domains = ['meijutt.com']
    start_urls = ['https://www.meijutt.com/alltop_hit.html']

    def parse(self, response):
        subSelector = response.xpath('//div[@class ="top-min"]')
        
        items= []
        
        for sub in subSelector:
            catgoryName = sub.xpath('.//div[@class="tt fn-clear"]/h5/text()').extract()[0] 
            storyNameTotal = sub.xpath('.//ul[@class ="top-list fn-clear"]/li/h5/a/text()').extract()
            rankpoint = sub.xpath('.//ul[@class ="top-list fn-clear"]/li/div[@class="lasted-num fn-left"]/i/text()').extract()
            point_int = sub.xpath('.//ul[@class ="top-list fn-clear"]/li/div[@class="lasted-time fn-right"]/strong/text()').extract()
            point_float = sub.xpath('.//ul[@class ="top-list fn-clear"]/li/div[@class="lasted-time fn-right"]/span/text()').extract()
            pointField = [float(a)+float(b) for a in point_int for b in point_float]
            
            for i in range(len(storyNameTotal)):
                item = Meiju100Item()
                item['catgory'] = catgoryName
                item["storyname" ] = storyNameTotal[i]
                item['rank'] = rankpoint[i]
                item['point'] = pointField[i]
                items.append(item) 
            
        return items  