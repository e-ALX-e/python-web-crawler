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
# driver.get("https://kns.cnki.net/kns8s/search?classid=WD0FTY92&kw=%E4%B8%9C%E7%9B%9F%20%26%20%E5%8D%AB%E6%98%9F&korder=SU")
# driver.get("www.AIAA.org")
driver.get("http://sjzk.spacespecial.com.cn/#/home/homePage")
