# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs


class Meiju100Pipeline(object):
    def process_item(self, item, spider):
        filename = 'movieRank.txt' 

        with codecs.open(filename,"a",'utf-8') as fp: 
            fp.write('%s\t%s\t%s\t%s\t\n'%(item["catgory"],item['storyname'],item['point'],item['rank']))
            
        return item
