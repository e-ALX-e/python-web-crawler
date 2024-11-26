import requests
import re
import json
from bs4 import BeautifulSoup
import csv
from lxml import etree
if __name__== "__main__":
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'  
    }

    i_page=130
    url=f"https://www.sciencedirect.com/journal/international-journal-of-applied-earth-observation-and-geoinformation/vol/{i_page}/suppl/C"
    resp=requests.get(url,headers=headers)
    xp_ht=etree.HTML(resp.text)
    xp_data=xp_ht.xpath('//html/body/div[4]/div/div/div/main/div//text()')
    # print(xp_data)
    with open ("C:\code\python\爬取的文档\\1231321321321.text",'w',encoding='utf-8')as fp:
        fp.write(resp.text)
