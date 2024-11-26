import requests  # 导入requests库，用于发送HTTP请求
import re  # 导入re库，用于正则表达式操作
import json  # 导入json库，用于处理JSON数据
from bs4 import BeautifulSoup  # 导入BeautifulSoup库，用于解析HTML文档
import csv  # 导入csv库，用于处理CSV文件

if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'
    }  # 设置请求头，模拟浏览器访问

    # 第二页的URL，第一页不可用
    url = 'http://www.asean-china-center.org/news/xwdt/2.html'
    response = requests.get(url=url, headers=headers)  # 发送GET请求获取网页内容

    # 解决乱码问题
    response.encoding = response.apparent_encoding  # 设置响应的编码
    response_soup = BeautifulSoup(response.text, 'lxml')  # 使用BeautifulSoup解析HTML内容

    # 查找所有符合条件的标题链接
    response_soup = str(response_soup)
    pattern = '<h3 class="title"><a href="(http://www.asean-china-center.org/.+/.+/\d+-\d+/\d+.html)" target="_blank">'
    response_soup = re.findall(pattern, response_soup)

    # 创建一个列表用于存储提取的数据
    extracted_data = []
    extracted_data_2 = []

    # 以下代码被注释掉，暂时不执行
    # with open('.\\爬取的文档\\test.text', 'w', encoding='utf-8') as fp:
    #     for i in response_soup:
    #         url_2 = i
    #         web_text = requests.get(url_2, headers=headers)
    #         web_text.encoding = web_text.apparent_encoding
    #         web_text_soup = BeautifulSoup(web_text.text, 'lxml')
    #         web_text_soup = web_text_soup.find('div', class_='mod-content')
    #         extracted_data.append()
    #         # print(web_text_soup.text, file=fp)
    #         print(i, 'ok')

    # print(len(response_soup))

    # 遍历每个链接，提取详细信息
    for i in response_soup:
        url_2 = i
        web_text = requests.get(url_2, headers=headers)  # 发送GET请求获取详细页面内容
        web_text.encoding = web_text.apparent_encoding  # 设置响应的编码
        web_text_soup = BeautifulSoup(web_text.text, 'lxml')  # 使用BeautifulSoup解析详细页面内容
        web_text_soup_1 = web_text_soup.find('div', class_='content_con')  # 查找文章内容部分

        # 提取文章文本
        web_tx_text = web_text_soup_1.text

        # 查找文章标题
        chinese_with_punctuation_pattern = re.compile(r'content_title">([\u4e00-\u9fa5，“0123456789”：；‘’【】{}——。；？！、《》（—）]+)</h1>')
        title = chinese_with_punctuation_pattern.findall(str(web_text_soup))

        # 查找文章发布时间
        time = re.findall('<span class="content_date">(202\d-\d*-\d*) \d*:?\d*:?\d*</span>', str(web_text_soup))

        # 查找文章来源
        made_t = re.findall('来源：([\u4e00-\u9fa5]+—?[\u4e00-\u9fa5]+)</span>', str(web_text_soup))

        # 查找文章作者
        maker_t = re.findall('作者：([\u4e00-\u9fa5]+—?[\u4e00-\u9fa5]+)</span>', str(web_text_soup))

        # 查找文章图片
        img = re.findall('<img alt="" src="(http://recdn.asean-china-center.org/img/\d+/\d+.j?p?n?g)"', str(web_text_soup))

        # 将提取的数据添加到列表中
        extracted_data.append(title[0])
        extracted_data.append(time[0])
        extracted_data.append(made_t[0])
        if len(maker_t) == 1:
            extracted_data.append(maker_t[0])
        else:
            extracted_data.append('无')
        extracted_data.append(web_tx_text)
        for i in img:
            extracted_data.append(i)
        extracted_data_2.append(extracted_data)
        extracted_data = []

    # 将提取的数据写入CSV文件
    with open('.\\爬取的文档\\test.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        # 写入表头
        csv_writer.writerow(['', 'Content'])
        # 写入提取的数据
        csv_writer.writerows(extracted_data_2)

    print('ok')