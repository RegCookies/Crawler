# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
class GetproxyPipeline(object):
    def process_item(self, item, spider):
        filename = 'proxy.txt'
        with codecs.open(filename,"a", 'utf-8') as fp:
            fp.write('%s\t%s\t%s\t%s\t%s\t%s\t\n'%(item['ip'],item['port'],item['ip_type'],
            item['location'],item['protocal'], item['sources']) )
        return item