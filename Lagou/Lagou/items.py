# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    city =  scrapy.Field()
    companyName = scrapy.Field()
    companyShortName = scrapy.Field()
    companySize = scrapy.Field() 
    district = scrapy.Field()
    education = scrapy.Field()
    jobNature = scrapy.Field()
    positionName = scrapy.Field()
    salaryMin = scrapy.Field()
    salaryMax = scrapy.Field()
    salaryAvg = scrapy.Field()
    positionAdvantage = scrapy.Field()
    
