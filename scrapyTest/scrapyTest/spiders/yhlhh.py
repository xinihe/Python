# -*- coding: utf-8 -*-
"""
Created on Mon May 14 14:43:56 2018

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Wed May  9 14:58:02 2018

@author: Administrator
"""

import scrapy
import re
from bs4 import BeautifulSoup


class tsSpride(scrapy.Spider):
    name = 'yh' # 爬虫的唯一名字，在项目中爬虫名字一定不能重复

    # start_requests() 必须返回一个迭代的Request
    def start_requests(self):
        # 待爬取的URL列表
       url_s ='http://www.eoeit.cn/lianhanghao/index.php?bank=&key=&province=&city=&page='
        # 模拟浏览器
       headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
       for i in range(1,6636):
           url=url_s+str(i)
           print(url)
           yield scrapy.Request(url=url, headers=headers, callback=self.parse)

    # 处理每个请求的下载响应
    def parse(self, response):
        soup = BeautifulSoup(response.body, 'html.parser')
        tb=soup.find("tbody")
        trs=tb.find_all('tr')
        for tr in trs:
            ylh=tr.find('td').next_sibling
            yhname=ylh.next_sibling
            yhtel=yhname.next_sibling
            yhaddr=yhtel.next_sibling
            #print(ylh.get_text(),yhname.get_text(),yhtel.get_text(),yhaddr.get_text())
        
            yield {  
                'ylh':ylh.get_text(),  # 图片
                'yhname':yhname.get_text(),  # title
                'yhtel':yhtel.get_text(),  # 发布时间
                'yhaddr': yhaddr.get_text(),  # 学历要求
            }
         
           
        
