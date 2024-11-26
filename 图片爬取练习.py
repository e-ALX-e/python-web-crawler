# 导入requests模块，用于发送HTTP请求
import requests
# 导入re模块，用于正则表达式匹配
import re
# 导入json模块，用于处理JSON数据
import json

if __name__ == "__main__":
    # 设置请求头，模拟浏览器访问
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'
    }
    # 初始化计数器
    jishu = 89
    # 设置请求的URL
    url = 'https://image.baidu.com/search/acjson'
    # 设置请求参数
    params = {
        'tn': 'resultjson_com',
        'logid': '8936465709811120571',
        'ipn': 'rj',
        'ct': '201326592',
        'is': '',
        'fp': 'result',
        'fr': '',
        'word': '神里绫华',
        'queryWord': '神里绫华',
        'cl': '2',
        'lm': '-1',
        'ie': 'utf-8',
        'oe': 'utf-8',
        'adpicid': '',
        'st': '-1',
        'z': '',
        'ic': '0',
        'hd': '',
        'latest': '',
        'copyright': '',
        's': '',
        'se': '',
        'tab': '',
        'width': '',
        'height': '',
        'face': '0',
        'istype': '2',
        'qc': '',
        'nc': '1',
        'expermode': '',
        'nojc': '',
        'isAsync': '',
        # 改变页数
        'pn': '120',
        'rn': '30',
        'gsm': '1e',
        '1715434782665': ''
    }
    # 发送GET请求
    response = requests.get(url, params=params, headers=headers)
    # 获取响应的文本内容
    st = response.text
    # 定义正则表达式模式，用于匹配图片URL
    pattern = 'https://img\d\.baidu\.com/it/u=\d+,\d+&fm=\d+&fmt=auto&app=\d+&f=JPEG\?w=\d+&h=\d+'
    # 使用正则表达式查找所有匹配的图片URL
    sbs = re.findall(pattern, st)
    # 去重
    sllh_list1 = list(set(sbs))
    # 打印去重后的图片URL数量
    print(len(sllh_list1))
    # 下载图片并保存到本地
    # for i in sllh_list1:
    #     with open(f'.\爬虫学习\图片爬取\神里绫华{jishu}.png', 'wb') as fp:
    #         jishu += 1
    #         url_2 = i
    #         fp.write(requests.get(url_2).content)

    # 打印完成信息
    print('ok')