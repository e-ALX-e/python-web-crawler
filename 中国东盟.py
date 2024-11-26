import requests
import re
import json
from bs4 import BeautifulSoup
import csv
import time
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

# 爬取页数
page___sum = 18

# 爬取的网址
# 新闻
# urlllll = 'http://www.asean-china-center.org/news/xwdt/'
# 教育
# urlllll = 'http://www.asean-china-center.org/education/jldt/'
# 贸易
# 9页
# urlllll = "http://www.asean-china-center.org/trade/dtmy/"
# 18页
urlllll = "http://www.asean-china-center.org/trade/jlhz/"

# 打开/绑定浏览器
options = Options()
options.add_experimental_option("debuggerAddress", "localhost:9222")
options.page_load_strategy = 'eager'
driver = webdriver.Chrome(options=options)

# 自动绑定浏览器
# driver = webdriver.Chrome()

# 数据IO
# updateAuthorData = UpdateAuthorData()

# 目录页
# driver.get("https://kns.cnki.net/kns8s/search?classid=WD0FTY92&kw=%E4%B8%9C%E7%9B%9F%20%E8%88%AA%E5%A4%A9&korder=SU")
# driver.get("https://kns.cnki.net/kns8s/search?classid=WD0FTY92&kw=%E4%B8%9C%E7%9B%9F%20%26%20%E9%81%A5%E6%84%9F&korder=SU")
# driver.get("https://kns.cnki.net/kns8s/search?classid=WD0FTY92&kw=%E4%B8%9C%E7%9B%9F%20%26%20%E5%8D%AB%E6%98%9F&korder=SU")
# driver.get("www.AIAA.org")
# driver.get("http://sjzk.spacespecial.com.cn/#/home/homePage")

# 打开CSV文件并定义字段名
# with open('C:\code\python\东盟_24_10_10.csv', 'w', newline='', encoding='utf-8') as csvfile:
#     fieldnames = ['标题', '作者', '来源', '时间', '内容', 'url']
#     csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     csv_writer.writeheader()

if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'
    }
    # 创建一个列表用于存储提取的数据
    extracted_data = []
    extracted_data_2 = []

    for k in range(1, page___sum + 1):
        # 第二页的URL，第一页不可用
        if k == 1:
            url = urlllll + f'index.html'
        else:
            url = urlllll + f'{k}.html'

        response = requests.get(url=url, headers=headers)
        # 解决乱码问题
        response.encoding = response.apparent_encoding
        response_soup = BeautifulSoup(response.text, 'lxml')
        
        # 提取所有文章链接
        response_soup = str(response_soup)
        pattern = '<h3 class="title"><a href="(http://www.asean-china-center.org/.+/.+/\d+-\d+/\d+.html)" target="_blank">'
        response_soup = re.findall(pattern, response_soup)

        for i in response_soup:
            kASD = []
            dic_sorce = {}
            url = i
            url_dic = {'url': i}
            dic_sorce.update(url_dic)
            
            driver.get(i)
            # time.sleep(3)
            
            # 获取标题
            title = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/h1').text
            dic_sorce.update({'标题': title})
            
            # 获取时间、来源、作者
            time_source = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]')
            c = time_source.text.split('\n')
            for i in c:
                if i[:2] == '来源':
                    dic_sorce.update({'来源': i})
                if i[:2] == '作者':
                    dic_sorce.update({'作者': i})
                if i[:2] == '20':
                    dic_sorce.update({'时间': i})
            if '来源' not in dic_sorce:
                dic_sorce.update({'来源': '中国—东盟中心'})
            if '作者' not in dic_sorce:
                dic_sorce.update({'作者': '中国—东盟中心'})
            
            # 获取文章内容
            content = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div[2]').text
            dic_sorce.update({'内容': content})
            kASD.append(dic_sorce)
            
            # 写入CSV文件
            with open('C:\code\python\东盟_24_10_10.csv', 'a', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['标题', '作者', '来源', '时间', '内容', 'url']
                csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                csv_writer.writerows(kASD)
                print("第", k, '页  ', url, '  完成')