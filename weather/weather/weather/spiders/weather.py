# -*- coding: utf-8 -*-
import scrapy
from weather.items import WeatherItem
import sys
class ShanghaiWeatherSpider(scrapy.Spider):
    name = 'weather'
    allowed_domains = ['shanghai.tianqi.com']
    start_urls = ['http://shanghai.tianqi.com/']

    def parse(self, response):
        items = []
        
        city =  response.xpath('//dd[@class="name"]/h2/text()').extract() 
        selector = response.xpath('//div[@class="day7"]')
        date = selector.xpath('ul[@class ="week"]/li/b/text()').extract()
        week = selector.xpath('ul[@class ="week"]/li/span/text()').extract()
        wind = selector.xpath('ul[@class ="txt"]/li/text()').extract() 
        weather = selector.xpath('ul[@class ="txt txt2"]/li/text()').extract()

        temperature1 = selector.xpath('div[@class="zxt_shuju"]/ul/li/span/text()').extract()

        temperature2 = selector.xpath('div[@class="zxt_shuju"]/ul/li/span/text()').extract()
        
        for i in range(7):
            item = WeatherItem()
            
            try:
                item['cityDate'] = city[0]+date[i] 
                item['week'] = week[i]
                item['wind'] = wind[i]
                item['temperature'] = temperature1[i] + '~' + temperature2[i]
                item['weather'] = weather[i]

            except IndexError:
                sys.exit(-1)
            items.append(item)
        return items 
