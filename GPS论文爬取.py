import requests
import re
import json
from bs4 import BeautifulSoup
import csv
from lxml import etree
import time

if __name__ == "__main__":
    # 设置请求头，模拟浏览器访问
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'
    }

    # 初始化存储提取数据的列表
    extracted_data_2 = []
    extracted_data = []

    # 循环遍历指定页数范围
    for page_alx in range(35, 42):
        # 构建每一页的URL
        url = f'https://link.springer.com/journal/10291/articles?utm_medium=display&utm_source=letpub&utm_content=text_link&utm_term=null&utm_campaign=MPSR_10291_AWA1_CN_CNPL_letpb_mp&page={page_alx}'
        
        # 发送HTTP请求获取页面内容
        resp = requests.get(url, headers=headers)
        
        # 使用lxml解析HTML内容
        et_gps = etree.HTML(resp.text)

        # 提取文章链接
        et_gps_xtml = et_gps.xpath('//*[@id="main"]/div/div/div/section/ol/li/article/div[1]/h3/a/@href')

        # 遍历每个文章链接
        for easdf in et_gps_xtml:
            # 构建文章详细页面的URL
            url_2 = easdf
            # url_2 = 'https://link.springer.com/article/10.1007/s10291-024-01660-4'
            
            # 发送HTTP请求获取文章详细内容
            resp_2 = requests.get(url_2, headers=headers)
            et_gps_2 = etree.HTML(resp_2.text)

            # 提取文章标题
            et_gps_title = et_gps_2.xpath('//*[@id="main"]/section/div/div/div[1]/h1//text()')
            extracted_data_2.append(et_gps_title)

            # 提取文章链接
            extracted_data_2.append(url_2)

            # 提取文章类型
            et_gps_leix = et_gps_2.xpath('//*[@id="main"]/section/div/div/div[1]/ul[1]/li[1]/text()')
            extracted_data_2.append(et_gps_leix)

            # 提取文章日期
            et_gps_day = et_gps_2.xpath('//*[@id="main"]/section/div/div/div[1]/ul[1]//time/text()')
            extracted_data_2.append(et_gps_day)

            # 提取作者信息
            et_gps_more = et_gps_2.xpath('//*[@id="main-content"]/main/div/header/ul/li/a/text()')
            extracted_data_2.append(et_gps_more)

            # 提取文章摘要
            et_gps_info = et_gps_2.xpath('//*[@id="Abs1-section"]//text()')
            extracted_data_2.append(et_gps_info)

            # 提取参考文献
            et_gps_from = et_gps_2.xpath('//*[@id="Bib1-content"]/div/ul/li/p[1]//text()')
            extracted_data_2.append(et_gps_from)

            # 提取资金信息
            et_gps_funding = et_gps_2.xpath('//*[@id="Fun-section"]//text()')
            extracted_data_2.append(et_gps_funding)

            # 提取作者单位信息
            et_gps_author_1 = et_gps_2.xpath('//*[@id="author-information-content"]/ol//text()')
            extracted_data_2.append(et_gps_author_1)

            # 提取作者贡献信息
            et_gps_author_2 = et_gps_2.xpath('//*[@id="author-information-content"]/p[1]/text()')
            extracted_data_2.append(et_gps_author_2)

            # 提取作者通信信息
            et_gps_author_3 = et_gps_2.xpath('//*[@id="corresponding-author-list"]//@href')
            extracted_data_2.append(et_gps_author_3)

            # 将提取的数据添加到主列表
            extracted_data.append(extracted_data_2)
            extracted_data_2 = []

            # 打印当前处理的文章链接
            print(easdf, 'ok')

        # 打印当前处理的页数
        print(page_alx, 'ok')

    # 将提取的数据写入CSV文件
    with open('.\\爬取的文档\\GPS论文第6部分.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        
        # 写入表头
        csv_writer.writerow(['文章标题', '文章链接', '文章类型', '文章日期', '参与者', '摘要', '参考文献', '资金', '作者信息_单位', '作者信息_贡献', '作者信息_通信'])
        
        # 写入提取的数据
        csv_writer.writerows(extracted_data)