# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
db_config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'db': 'pytest',
    'charset': 'utf8'
}

class ScrapytestPipeline(object):
    def __init__(self):
        self.connection = connection = pymysql.connect(**db_config)
        self.cursor = self.connection.cursor()
    def process_item(self, item, spider):
       # sql = 'insert into aliinfo(pic, title, alihref, price, bcount, aliid) values(%s, %s, %s, %s, %s, %s)'
        sql = 'insert into yhinfo(ylh, yhname,yhtel,yhaddr) values(%s, %s, %s, %s)'
        try:
            self.cursor.execute(sql, (item['ylh'].encode('utf-8'),
                                      item['yhname'].encode('utf-8'),
                                      item['yhtel'].encode('utf-8'),
                                      item['yhaddr'].encode('utf-8')
                                      )
                                )
            self.connection.commit()
        except pymysql.Error as e:
            # 若存在异常则抛出
            print(e.args)
        return item
