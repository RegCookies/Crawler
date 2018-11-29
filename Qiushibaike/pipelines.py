# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import time
import urllib.request
import os 
import sys
import codecs 
class QiushibaikePipeline(object):
    def process_item(self, item, spider):
        filename ="qiubai.txt"
        imDir = 'img'
        if os.path.isdir(imDir): 
            pass
        else:
            os.mkdir(imDir)

        with codecs.open(filename,"a" , 'utf-8') as fp : 
            fp.write("-"*50 + '\n' + '*'*50 + '\n')
            fp.write("author: \t %s\n"%(item['author']))
            fp.write("content: \t %s\n"%(item['content'])) 


            try:
                imgURL = item['img'][1]
            except IndexError:
                pass

            else: 
                imgName = os.path.basename(imgURL)
                fp.write("img:\t%s\n"%(imgName))
                imgPathName = imDir + os.sep + imgName 
                with open(imgPathName , "wb") as fp: 
                    response = urllib.request.urlopen(imgURL)
                    fp.write(response.read())
            fp.write("fun: %s\t talk:%s\n"%(item['funNum'],item['talkNum'])) 
            fp.write("-"*50 + '\n' + '*'*50 + '\n')
        return item
