# 导入requests库，用于发送HTTP请求
import requests  
# 导入re模块，用于正则表达式操作
import re  
# 导入json模块，用于处理JSON数据
import json  
# 导入BeautifulSoup库，用于解析HTML文档
from bs4 import BeautifulSoup  
# 导入csv模块，用于处理CSV文件
import csv  
# 导入lxml库，用于解析XML和HTML文档
from lxml import etree  

if __name__ == "__main__":
    # 设置请求头，模拟浏览器访问
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'
    }  

    # 定义目标URL
    url = 'https://sy.zu.anjuke.com/map/ajax/pclist/Api_get_house_list?refer_url=&p=1&maxp=99&room_num=0&price_id=0&rent_type=0&price_min=0&price_max=0&lx_id=&tag_id=&orient_id=&order_id=0&lat=18.306554_18.323508&lng=109.511939_109.572987&zoom=16&community_id=100590915&ib=1&et=c1189b&bst=pzm134'

    # 发送GET请求获取响应
    resp = requests.get(url, headers=headers)  

    # 初始化一个空列表，用于存储价格信息
    appppp = []  
    # 打开文件，准备写入价格信息
    with open('.\爬取的文档\\58二手房_price_2.text', 'w', encoding='utf-8') as fp:
        # 解析响应内容为JSON对象
        ask = resp.json()  
        # 获取JSON对象中的"val"字段
        ask = ask["val"]  
        # 获取"val"字段中的"props"字段
        ask = ask["props"]  
        # 遍历每个房源信息，提取价格并添加到列表中
        for i in ask:
            appppp.append(i["price"])  
        # 对价格列表进行排序
        appppp.sort()  
        # 将排序后的价格信息写入文件
        for i in appppp:
            print('价格：', i, file=fp)  
    # 打印完成提示
    print('ok')  