import requests
if __name__== "__main__":
    #指定url
    url = 'https://www.bilibili.com/'
    #发起请求
    response = requests.get(url=url)
    #获取响应数据
    page_text = response.text
    print(page_text)
    print(response.status_code)
    #存储
    # with open ('./bilibili.html','w',encoding='utf-8') as fp:
    #     fp.write(page_text)
    # print('爬取数据结束3')