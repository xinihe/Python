# -*- coding: utf-8 -*-
"""
Created on Wed May  9 10:50:50 2018

@author: Administrator
"""

from urllib import request
from bs4 import BeautifulSoup
import pymysql

# mysql连接信息（字典形式）
db_config ={
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'db': 'pytest',
    'charset': 'utf8'
}
# 获得数据库连接
#connection = pymysql.connect(db_config)

# 数据库配置，获得连接（参数方式）
connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='pytest', charset='utf8')
url = r'http://www.jianshu.com/'

# 模拟浏览器头
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
page = request.Request(url, headers=headers)
page_info = request.urlopen(page).read().decode('utf-8')
soup = BeautifulSoup(page_info, 'html.parser')
urls = soup.find_all('a', 'title')

try:
    # 获得数据库游标
    with connection.cursor() as cursor:
        sql = 'insert into titles(title, url) values(%s, %s)'
        for u in urls:
            # 执行sql语句
            print(u)
            cursor.execute(sql, (u.string, r'http://www.jianshu.com'+u.attrs['href']))
    # 事务提交
    connection.commit()
finally:
    # 关闭数据库连接
    connection.close()