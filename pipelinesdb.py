# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import codecs
import mysql.connector
class WeatherPipeline(object):
    def process_item(self, item, spider):
        
        mydb = mysql.connector.connect(
            host = 'localhost',
            user  ="root",
            passwd ="root",
            database ='scrapyDB' 
        )
        mycursor = mydb.cursor() 
        
        sql = "INSERT INTO weather(cityDate,week,temperature,weather,wind) VALUES(%s, %s, %s, %s,%s)" 
        val = (item['cityDate'],item['week'],item['temperature'], item['weather'], item['wind']) 
        mycursor.execute(sql,val)
        mydb.commit() 
        mycursor.close()
        mydb.close()
        
        #filename = '天气db.txt'

        #with codecs.open(filename, 'a', 'utf-8') as fp:
            #fp.write("%s\t%s\t%s\t%s\t%s\n"%(item['cityDate'],item['week'],item['temperature'], item['weather'],item['wind'])) 
        return item       
