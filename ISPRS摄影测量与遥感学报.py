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
    url="https://www.sciencedirect.com/journal/isprs-journal-of-photogrammetry-and-remote-sensing/vol/212/suppl/C" 
    resp=requests.get(url,headers=headers).text
    
    xps=etree.HTML(resp)
    alx=xps.xpath('//html/body/div[4]/div/div/div/main/section[2]/div/div/div/form/div/div[2]/ol/li[1]/dl/dt/h3//@href')
    print(alx)
    print(resp)
    