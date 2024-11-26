# 导入requests模块，用于发送HTTP请求
import requests

# 主程序入口
if __name__ == "__main__":
    # 百度翻译API的URL
    url = 'https://fanyi.baidu.com/ait/text/translate'
    
    # 请求参数
    params = {
        'query': "dog",  # 要翻译的文本
        'from': "en",    # 源语言
        'milliTimestamp': 1715236069909  # 时间戳，用于防缓存
    }
    
    # 请求头，模拟浏览器访问
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'
    }
    
    # 发送POST请求
    response = requests.post(url=url, params=params, headers=headers)
    
    # 打印响应内容
    print(response.text)