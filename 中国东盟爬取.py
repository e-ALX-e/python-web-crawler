import requests
import re
import json
from bs4 import BeautifulSoup
import csv

if __name__ == "__main__":
    # 设置请求头，模拟浏览器访问
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'
    }
    # 创建一个列表用于存储提取的数据
    extracted_data = []
    extracted_data_2 = []
    
    # 循环遍历100到102页
    for k in range(100, 103):
        # 构建每一页的URL
        url = f'http://www.asean-china-center.org/news/xwdt/{k}.html'
        # 发送HTTP请求获取页面内容
        response = requests.get(url=url, headers=headers)
        
        # 解决乱码问题
        response.encoding = response.apparent_encoding
        
        # 使用BeautifulSoup解析HTML内容
        response_soup = BeautifulSoup(response.text, 'lxml')
        
        # 查找所有符合条件的标题链接
        response_soup.find_all("div>div>div>div>div>div>div>div>h3>a", class_='title')
        
        # 将BeautifulSoup对象转换为字符串
        response_soup = str(response_soup)
        
        # 使用正则表达式提取标题链接
        pattern = '<h3 class="title"><a href="(http://www.asean-china-center.org/.+/.+/\d+-\d+/\d+.html)" target="_blank">'
        response_soup = re.findall(pattern, response_soup)
        
        # 遍历提取的链接
        for s_i in response_soup:
            url_2 = s_i
            # 发送HTTP请求获取文章详细内容
            web_text = requests.get(url_2, headers=headers)
            
            # 解决乱码问题
            web_text.encoding = web_text.apparent_encoding
            
            # 使用BeautifulSoup解析HTML内容
            web_text_soup = BeautifulSoup(web_text.text, 'lxml')
            
            # 查找文章内容部分
            web_text_soup_1 = web_text_soup.find('div', class_='content_con')
            
            # 提取文章文本
            web_tx_text = web_text_soup_1.text
            
            # 查找文章内容部分
            web_text_soup = web_text_soup.find('div', class_='mod-content')
            
            # 定义正则表达式模式，用于匹配带有标点符号的中文字符
            chinese_with_punctuation_pattern = re.compile(r'content_title">([\u4e00-\u9fa5，“、”：；‘’【】$￥%…&`~^.><—。-；？！、《》（）]+)</h1>')
            
            # 使用findall函数查找文本中所有的匹配项
            title = chinese_with_punctuation_pattern.findall(str(web_text_soup))
            
            # 提取时间
            time = re.findall('<span class="content_date">(20\d\d-\d*-\d*) \d*:?\d*:?\d*</span>', str(web_text_soup))
            
            # 提取来源
            made_t = re.findall('来源：([\u4e00-\u9fa5]+—?[\u4e00-\u9fa5]+)</span>', str(web_text_soup))
            
            # 提取作者
            maker_t = re.findall('作者：([\u4e00-\u9fa5]+—?[\u4e00-\u9fa5]+)</span>', str(web_text_soup))
            
            # 提取图片
            img = re.findall('<img alt="" src="(http://recdn.asean-china-center.org/img/\d+/\d+.j?p?n?g)"', str(web_text_soup))
            
            # 处理提取的数据
            if len(title) == 1:
                extracted_data.append(title[0])
            else:
                extracted_data.append('无')
            
            if len(time) == 1:
                extracted_data.append(time[0])
            else:
                extracted_data.append('无')
            
            if len(made_t) == 1:
                extracted_data.append(made_t[0])
            else:
                extracted_data.append('无')
            
            if len(maker_t) == 1:
                extracted_data.append(maker_t[0])
            else:
                extracted_data.append('无')
            
            extracted_data.append(web_tx_text)
            extracted_data.append(url_2)
            
            for i in img:
                extracted_data.append(i)
            
            extracted_data_2.append(extracted_data)
            extracted_data = []
        
        # 打印当前页数
        print(f'第{k}页结束')

    # 将提取的数据写入CSV文件
    with open('.\\爬取的文档\\test3 .csv', 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        # 写入表头
        csv_writer.writerow(['标题', '时间', '来源', '作者', '正文', '文章链接', '图片'])
        # 写入提取的数据
        csv_writer.writerows(extracted_data_2)