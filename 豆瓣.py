# 导入requests模块，用于发送HTTP请求
import requests
# 导入json模块，用于处理JSON数据
import json

if __name__ == "__main__":
    # 设置请求头，模拟浏览器访问
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'
    }
    
    # 设置请求URL，获取豆瓣热门电视剧数据
    url = 'https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0'
    
    # 发送GET请求
    response = requests.get(url=url, headers=headers)
    
    # 解析响应的JSON数据
    lis = response.json()

    # 打开文件，准备写入JSON数据
    with open('.\爬取的文档\豆瓣.json', 'w', encoding='utf-8') as fp:
        # 将解析后的JSON数据写入文件
        json.dump(lis, fp, ensure_ascii=False, indent=4)
    
    # 打印解析后数据的类型
    print(type(lis))