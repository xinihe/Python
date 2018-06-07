# -*- coding: utf-8 -*-
"""
Created on Tue May 15 13:12:52 2018

@author: Administrator
"""

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
def get_ip():
    '''获取代理IP'''
    url = 'http://www.xicidaili.com/nn'
    my_headers = {
        'Accept': 'text/html, application/xhtml+xml, application/xml;',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Referer': 'http: // www.xicidaili.com/nn',
        'User-Agent': 'Mozilla / 5.0(Windows NT 6.1;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 45.0.2454.101Safari / 537.36'
    }
    r = requests.get(url,headers=my_headers)
    soup = BeautifulSoup(r.text,'html.parser')
    data = soup.find_all('td')

    #定义IP和端口Pattern规则
    ip_compile = re.compile(r'<td>(\d+\.\d+\.\d+\.\d+)</td>')  #匹配IP
    port_compile = re.compile(r'<td>(\d+)</td>')  #匹配端口
    ip = re.findall(ip_compile,str(data))    #获取所有IP
    port = re.findall(port_compile,str(data))  #获取所有端口
    z = [':'.join(i) for i in zip(ip,port)]  #列表生成式
    print(z)
    #组合IP和端口
    return z

# 设置user-agent列表,每次请求时，随机挑选一个user-agent

ua_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60",
        "Opera/8.0 (Windows NT 5.1; U; en)",
        "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
        "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2 ",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)",
    ]
def get_url(url,code=0,ips=[]):
    '''
    投票
    如果因为代理IP已失效造成投票失败，则会自动换一个代理IP后继续投票
    :param code:
    :param ips:
    :return:
    '''
    try:
        ip = choice(ips)
    except:
        return False

    else:
        #指定代理IP
        proxies = {
            'http':ip
        }
        headers = {
            'Content-Type': 'text/html; charset=UTF-8',
            'Host': 'www.eoeit.cn',
            'Referer':'http://www.eoeit.cn/lianhanghao/index.php?bank=&key=&province=%E6%B5%99%E6%B1%9F%E7%9C%81&city=&page=',
            'User-Agent':choice(ua_list)
        }

    try:
        yield scrapy.Request(url=url, headers=headers, callback=self.parse, proxies=proxies)
       
    except requests.exceptions.ConnectionError:
        print('ConnectionError')
        if not ips:
            print('ip 已失效')
            sys.exit()
        #删除不可用的代理IP
        if ip in ips:
            ips.remove(ip)
        #重新请求url
        get_url(url,code=0,ips=[])
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
            #启动线程，每隔1s产生一个线程，可通过控制时间加快投票速度
           t1 = threading.Thread(target=get_url,args=(url,i,ips))
           t1.start()
           time.sleep(1)  #time.sleep的最小单位是毫秒

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
         
           
        
