# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapytestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field() 
    '''
    pic = scrapy.Field()  # 工作地点
    title = scrapy.Field()    # 最低薪资
    alihref = scrapy.Field()   # 公司名称
    price = scrapy.Field()      # 信息发布时间
    bcount = scrapy.Field()     # 学历要求
    aliid = scrapy.Field()     # 职位
    '''
    ylh = scrapy.Field()  # 银行联行号
    yhname = scrapy.Field()    # 银行名称
    yhtel = scrapy.Field()    # 银行名称
    yhaddr = scrapy.Field()    # 银行名称