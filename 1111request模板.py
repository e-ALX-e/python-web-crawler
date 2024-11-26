# 导入requests模块，用于发送HTTP请求
import requests
# 导入re模块，用于正则表达式操作
import re
# 导入json模块，用于处理JSON数据
import json
# 导入BeautifulSoup类，用于解析HTML和XML文档
from bs4 import BeautifulSoup
# 导入csv模块，用于处理CSV文件
import csv
# 导入etree模块，用于解析XML和HTML文档
from lxml import etree

# 主程序入口
if __name__ == "__main__":
    # 设置请求头，模拟浏览器访问
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'
    }