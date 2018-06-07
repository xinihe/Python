# -*- coding: utf-8 -*-
"""
Created on Wed May  9 14:58:02 2018

@author: Administrator
"""

import scrapy
import re
from bs4 import BeautifulSoup


class tsSpride(scrapy.Spider):
    name = 'ali' # 爬虫的唯一名字，在项目中爬虫名字一定不能重复

    # start_requests() 必须返回一个迭代的Request
    def start_requests(self):
        # 待爬取的URL列表
       urls = ['https://cntianxingjian.1688.com/page/offerlist.htm',
               'https://cntianxingjian.1688.com/page/offerlist.htm&pageNum=2',
               'https://cntianxingjian.1688.com/page/offerlist.htm&pageNum=3',
               'https://cntianxingjian.1688.com/page/offerlist.htm&pageNum=4',
               'https://cntianxingjian.1688.com/page/offerlist.htm&pageNum=5',
               'https://cntianxingjian.1688.com/page/offerlist.htm&pageNum=6',
                ]
        # 模拟浏览器
       headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
       for url in urls:
            yield scrapy.Request(url=url, headers=headers, callback=self.parse)

    # 处理每个请求的下载响应
    def parse(self, response):
        soup = BeautifulSoup(response.body, 'html.parser')
        uls=soup.find_all('ul', 'offer-list-row')
        for ul in uls:
            for info in ul.find_all('li'):
                aid=info.attrs['data-prop']
                d1 = eval(aid)
                # 存储爬取的信息
                yield {
                    
                    'pic': (info.find('img')).attrs['data-lazy-load-src'],  # 图片
                    'title': info.find('a')['title'],  # title
                    'alihref':info.find('a')['href'],  # 发布时间
                    'price': info.find('em').get_text(),  # 学历要求
                    'bcount': info.find('span','booked-counts').get_text(),  # 公司名称
                    'aliid': d1['offer_id'],  # aliid
                }
