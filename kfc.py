import requests
import re
import json
from bs4 import BeautifulSoup
import csv
from lxml import etree

if __name__ == "__main__":
    # 设置请求头，模拟浏览器访问
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'
    }
    
    # 定义请求的URL
    url = 'https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    
    # 循环遍历1到10页
    for page in range(1, 11):
        # 定义请求参数
        params = {
            'cname': '三亚',  # 城市名称
            'pid': '',  # 父级ID
            'pageIndex': page,  # 当前页码
            'pageSize': '10',  # 每页显示的数量
        }
        
        # 发送POST请求获取响应内容
        response = requests.post(url=url, params=params, headers=headers).text
        
        # 打印响应内容
        print(response)
        print()