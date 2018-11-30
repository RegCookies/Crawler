# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs 
import mysql.connector
class LagouPipeline(object):
    def process_item(self, item, spider):
        filename = "求职.txt"
        with codecs.open(filename,'a', 'utf-8') as fp:
            fp.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t\n"%(item['city'],
            item['companyName'],
            item['companyShortName'],item['companySize'],item['district'],
            item['education'],item['jobNature'],item['positionName'],item['salaryMax'],item['salaryMin'],item['salaryAvg'], 
            item['positionAdvantage']))

        
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database = 'job' 
        )

        mycursor = mydb.cursor()
        
        #mycursor.execute("CREATE TABLE jobs (city VARCHAR(50),companyName VARCHAR(50),companyShortName VARCHAR(50),companySize VARCHAR(50),district VARCHAR(50),education VARCHAR(50),jobNature VARCHAR(50),positionName VARCHAR(50),salaryMax VARCHAR(50), salaryMin VARCHAR(50),salaryAvg VARCHAR(50), positionAdvantage VARCHAR(50))")
        #mycursor.execute("CREATE DATABASE mydatabase")
        sql = "INSERT INTO jobs (city,companyName,companyShortName,companySize,district,education,jobNature,positionName,salaryMin,salaryMax,salaryAvg,positionAdvantage) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        val = (item['city'],
            item['companyName'],
            item['companyShortName'],item['companySize'],item['district'],
            item['education'],item['jobNature'],item['positionName'],item['salaryMax'],item['salaryMin'],item['salaryAvg'], 
            item['positionAdvantage'])
        
        mycursor.execute(sql,val)
        mydb.commit()

        return item
