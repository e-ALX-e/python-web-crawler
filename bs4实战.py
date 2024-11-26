import requests
import re
from bs4 import BeautifulSoup

if __name__ == "__main__":
    # 设置请求头，模拟浏览器访问
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'
    }
    
    # 构建搜索页面的URL
    url = 'https://link.springer.com/search?new-search=true&query=remote+sensing++OR+RS&sortBy=relevance&content-type=Article&dateFrom&dateTo'
    
    # 发送HTTP请求获取搜索结果页面
    sp_text = requests.get(url, headers=headers)
    
    # 使用BeautifulSoup解析HTML内容
    soup = BeautifulSoup(sp_text.text, 'lxml')
    
    # 查找所有符合条件的标题
    soup_t = soup.find_all('h3', class_='app-card-open__heading')
    
    # 将BeautifulSoup对象转换为字符串
    str_soup_t = str(soup_t)
    
    # 使用正则表达式提取文章链接
    str_soup_list = re.findall('href="(.+)"', str_soup_t)
    
    # 打印提取的文章链接
    print(str_soup_list)
    
    # 构建第一个文章的详细页面URL
    url_2 = 'https://link.springer.com/' + str_soup_list[0]
    
    # 发送HTTP请求获取文章详细内容
    soup_t2 = requests.get(url_2, headers=headers)
    
    # 将文章详细内容写入文件
    with open('.\\爬取的文档\\论文文档.text', 'w', encoding='utf-8') as fp:
        # 提取并打印文章的纯文本内容
        print(BeautifulSoup(soup_t2.text).get_text(), file=fp)