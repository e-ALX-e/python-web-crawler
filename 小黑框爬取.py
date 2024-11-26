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

# 配置Chrome选项
# 打开/绑定浏览器
options = Options()
options.add_experimental_option("debuggerAddress", "localhost:9222")
options.page_load_strategy = 'eager'
driver = webdriver.Chrome(options=options)

# 自动绑定浏览器
# driver = webdriver.Chrome()

# 数据IO
# updateAuthorData = UpdateAuthorData()

# 报错退出函数
def errorOperate():
    exit

# 读取列表
driver.get('https://sat.huijiwiki.com/wiki/%E5%BC%95%E5%AF%BC%E9%A1%B5:%E4%B8%AD%E5%9B%BD%E7%9A%84%E6%8A%80%E6%9C%AF%E8%AF%95%E9%AA%8C%E5%8D%AB%E6%98%9F')
for i in range(3):
    time.sleep(10)  # 等待页面加载
    alxdat = driver.find_elements(by=By.XPATH, value=f'//*[@id="mw-content-text"]/div/center[3]/div/table/tbody/tr[{i+1}]/td[1]/a')
    print(alxdat)  # 打印找到的元素
    time.sleep(10)  # 等待页面加载
    alxdat[0].click()  # 点击第一个元素
    print(alxdat)  # 打印点击后的元素
    print('ok')  # 打印确认信息
    time.sleep(10)  # 等待页面加载
    lis = []
    for i in range(30):
        bk_weix = driver.find_elements(by=By.XPATH, value=f'//*[@id="mw-content-text"]/div/table/tbody/tr[{i}]')
        if len(bk_weix) > 0:
            lis.append(bk_weix[0].text)  # 提取文本并添加到列表
    print(lis)  # 打印列表
    sumdic = []
    for i in lis:
        i_bk = i.split(' ')
        if len(i_bk) >= 2:
            acc = {i_bk[0]: ''.join(i_bk[1:])}
            sumdic.append(acc)  # 构建字典并添加到列表
    print(sumdic)  # 打印字典列表

# for page in range(1, 180):

    # # 等待加载完毕
    # time.sleep(1)
    # alldata = driver.find_elements(by=By.XPATH, value='//*[@id="body"]/div/div/div[2]/div[4]/div/dl/dt/a')
    # for ele in alldata:
    #     ssr = []
    #     ssr.append("标题")
    #     ssr.append(ele.text)  # 添加标题
    #     # ele.click()
    #     lis_1 = []
    #     driver.get(ele.get_attribute('href'))  # 打开链接
    #     # 等待加载完毕
    #     time.sleep(1)

    #     ssr.append("url")
    #     ssr.append(driver.current_url)  # 添加URL
    #     print(ssr)

    #     # 解析目录
    #     panduan = driver.find_elements(by=By.XPATH, value='//*[@id="body"]/div/div[3]/div[2]/p[1]')
    #     # Title = driver.find_elements(by=By.LINK_TEXT, value='专利类型：')
    #     # Title = driver.find_elements(by=By.CSS_SELECTOR, value='.rticle-detail.flength7 p')

    #     z_all = driver.find_elements(by=By.XPATH, value='//*[@id="body"]/div/div[3]/div[1]')
    #     for i in z_all:
    #         print(i.text)  # 打印文本
    #     s = z_all[0].text
    #     ssr2 = s.split('\n')
    #     ssr += ssr2  # 添加解析后的文本
    #     print(ssr)
    #     # # 将提取的数据写入CSV文件
    #     # with open('.\\爬取的文档\\航天行星探测专利.csv', 'a', newline='', encoding='utf-8') as csvfile:
    #     #     csv_writer = csv.writer(csvfile)
    #     #     # 写入提取的数据
    #     #     csv_writer.writerow(ssr)
    #     # 返回（后退）
    #     driver.back()
    #     # 等待加载完毕
    #     time.sleep(1)
    # print(f'第{page}页完成')