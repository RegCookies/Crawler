# -*- coding: utf-8 -*-
import scrapy


class QiubaiSpider(scrapy.Spider):
    name = 'Qiubai'
    allowed_domains = ['www.qiushibaike.com/hot/']
    start_urls = ['http://www.qiushibaike.com/hot/']

    def parse(self, response):
        pass 