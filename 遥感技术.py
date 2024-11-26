# from updateAuthorData import UpdateAuthorData

# 导入时间模块，用于控制程序执行的时间间隔
import time

# 导入Selenium相关的异常处理模块，用于捕获页面元素不存在或不可交互的异常
from selenium.common import NoSuchElementException, ElementNotInteractableException

# 导入Selenium WebDriver模块，用于自动化浏览器操作
from selenium import webdriver

# 导入Selenium WebDriver的By类，用于定位页面元素
from selenium.webdriver.common.by import By

# 导入Selenium WebDriver的Chrome选项配置模块，用于设置Chrome浏览器的启动参数
from selenium.webdriver.chrome.options import Options

# 导入Selenium WebDriver的WebDriverWait类，用于等待页面元素加载
from selenium.webdriver.support.ui import WebDriverWait

# 导入CSV模块，用于处理CSV文件的读写操作
import csv

# 打开/绑定浏览器
options = Options()
options.add_experimental_option("debuggerAddress", "localhost:9222")
options.page_load_strategy = 'eager'
driver = webdriver.Chrome(options=options)

# 自动绑定浏览器
# driver = webdriver.Chrome()

# 数据IO
# updateAuthorData = UpdateAuthorData()

# 目录页
# driver.get("https://kns.cnki.net/kns8s/search?classid=WD0FTY92&kw=%E4%B8%9C%E7%9B%9F%20%E8%88%AA%E5%A4%A9&korder=SU")
# driver.get("https://kns.cnki.net/kns8s/search?classid=WD0FTY92&kw=%E4%B8%9C%E7%9B%9F%20%26%20%E9%81%A5%E6%84%9F&korder=SU")
# driver.get("https://zlf.cqvip.com/zk/search.aspx?from=index&key=U%3D%E9%81%A5%E6%84%9F&page=3&ids=")


def errorOperate():
    exit

# sorse="https://zlf.cqvip.com/zk/search.aspx?from=index&key=U%3D%E9%81%A5%E6%84%9F&page=2&ids="



# 读取列表

for page in range(1,180):
    # driver.get(f"https://zlf.cqvip.com/zk/search.aspx?from=index&key=U%3D%E9%81%A5%E6%84%9F&page={page}&ids=")
    # driver.get(f"https://zlf.cqvip.com/zk/search.aspx?from=index&key=U%3D%E9%81%A5%E6%84%9F&page={page}&ids=&cf=ZY%3D27%23%E8%88%AA%E7%A9%BA%E5%AE%87%E8%88%AA%E7%A7%91%E5%AD%A6%E6%8A%80%E6%9C%AF%5B_%5DZY%3D19%23%E7%94%B5%E5%AD%90%E7%94%B5%E4%BF%A1%5B_%5DZY%3D10%23%E5%A4%A9%E6%96%87%E5%9C%B0%E7%90%83%5B_%5DSCC%3D3910216%23%E5%8D%AB%E6%98%9F")
    # driver.get(f"https://zlf.cqvip.com/zk/search.aspx?from=zk_search&key=U%3D%E7%81%AB%E7%AE%AD&page={page}&cf=SCC%3D3910954%23%E5%8D%AB%E6%98%9F%E5%8F%91%E5%B0%84%5B_%5DSCC%3D5596651%23%E7%81%AB%E7%AE%AD%E5%8F%91%E5%B0%84%5B_%5DSCC%3D3910216%23%E5%8D%AB%E6%98%9F%5B_%5DSCC%3D6419153%23%E8%88%AA%E5%A4%A9%5B_%5DSCC%3D5596513%23%E7%81%AB%E7%AE%AD&ids=")
    driver.get(f"https://zlf.cqvip.com/zk/search.aspx?from=zk_search&key=U%3D%E8%A1%8C%E6%98%9F%E6%8E%A2%E6%B5%8B&page={page}&ids=")
    # 等待加载完毕
    time.sleep(1)
    alldata = driver.find_elements(by=By.XPATH, value='//*[@id="body"]/div/div/div[2]/div[4]/div/dl/dt/a')
    for ele in alldata:
        ssr=[]
        ssr.append("标题")
        ssr.append(ele.text)
        # ele.click()
        lis_1=[]
        driver.get(ele.get_attribute('href'))
        # 等待加载完毕
        time.sleep(1)

        ssr.append("url")
        ssr.append(driver.current_url)
        print(ssr)
        
        # 解析目录
        panduan = driver.find_elements(by=By.XPATH, value='//*[@id="body"]/div/div[3]/div[2]/p[1]')
        # Title = driver.find_elements(by=By.LINK_TEXT,value='专利类型：')
        # Title = driver.find_elements(by=By.CSS_SELECTOR,value='.rticle-detail.flength7 p')


        z_all = driver.find_elements(by=By.XPATH, value='//*[@id="body"]/div/div[3]/div[1]')
        for i in z_all:
            print(i.text)
        s=z_all[0].text
        ssr2=s.split('\n')
        ssr+=ssr2
        print(ssr)
        # # 将提取的数据写入CSV文件
        # with open('.\\爬取的文档\\航天行星探测专利.csv', 'a', newline='', encoding='utf-8') as csvfile:
        #     csv_writer = csv.writer(csvfile)
        #     # 写入提取的数据
        #     csv_writer.writerow(ssr) 
        #返回（后退）
        driver.back()
        # 等待加载完毕
        time.sleep(1)
    print(f'第{page}页完成')










