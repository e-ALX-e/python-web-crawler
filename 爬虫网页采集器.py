# 导入requests库，用于发送HTTP请求
import requests

# 主程序入口
if __name__ == "__main__":
    # 搜索页面的URL
    url = 'https://www.baidu.com/s'
    # url = 'https://image.baidu.com/s'
    
    # 获取用户输入的搜索关键词
    pt = input('请输入你要搜索的东西')
    
    # 设置User-Agent，进行UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'
    }
    
    # 设置请求参数
    param = {
        'word': pt
    }
    
    # 生成保存文件的路径
    fl = '.\链接爬取\\' + pt + '.html'
    
    # 发送GET请求
    response = requests.get(url=url, params=param, headers=headers)
    
    # 将响应内容写入文件
    with open(fl, 'w', encoding='utf-8') as fs:
        fs.write(response.text)
    
    # 输出提示信息
    print('ok')

    # 示例HTML片段，用于参考
    # <a href="http://image.baidu.com/i?tn=baiduimage&amp;ps=1&amp;ct=201326592&amp;lm=-1&amp;cl=2&amp;nc=1&amp;ie=utf-8&amp;dyTabStr=MCwxLDMsMiw0LDYsNSw4LDcsOQ%3D%3D&amp;word=789" sync="" wdfield="word" class="s-tab-item s-tab-item_1CwH- s-tab-pic_p4Uej s-tab-pic">图片</a>