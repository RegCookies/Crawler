# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import codecs
import json

class WeatherPipeline(object):
    def process_item(self, item, spider):
        filename = '天气json.txt'
        with codecs.open(filename, 'a', 'utf-8') as fp:
            jsonstr = json.dumps(dict(item))
            fp.write("%s\r\n"%jsonstr)
        return item
