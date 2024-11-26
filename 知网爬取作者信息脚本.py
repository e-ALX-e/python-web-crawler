from updateAuthorData import UpdateAuthorData

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

# 配置Chrome浏览器的启动参数
options = Options()
options.add_experimental_option("debuggerAddress", "localhost:9222")
options.page_load_strategy = 'eager'

# 创建WebDriver实例并绑定到已打开的浏览器
driver = webdriver.Chrome(options=options)

# 自动绑定浏览器
# driver = webdriver.Chrome()

# 数据IO
# updateAuthorData = UpdateAuthorData()

# 访问知网搜索页面
# driver.get("https://kns.cnki.net/kns8s/search?classid=WD0FTY92&kw=%E4%B8%9C%E7%9B%9F%20%E8%88%AA%E5%A4%A9&korder=SU")
# driver.get("https://kns.cnki.net/kns8s/search?classid=WD0FTY92&kw=%E4%B8%9C%E7%9B%9F%20%26%20%E9%81%A5%E6%84%9F&korder=SU")
driver.get("https://kns.cnki.net/kns8s/search?classid=WD0FTY92&kw=%E4%B8%9C%E7%9B%9F%20%26%20%E5%8D%AB%E6%98%9F&korder=SU")

def errorOperate():
    # 定义错误处理函数
    exit

# 读取列表
while True:
    # 等待页面加载完毕
    time.sleep(2)
    
    # 点击显示所有作者的按钮
    moreAuthor = driver.find_elements(by=By.CSS_SELECTOR, value=".showAllAuthors")
    for ele in moreAuthor:
        ele.click()
    
    # 等待作者信息加载完毕
    time.sleep(1)

    # 解析目录页中的论文列表
    paperList = driver.find_elements(by=By.CSS_SELECTOR, value="table.result-table-list tbody tr")
    
    # 遍历每篇论文
    for i in range(len(paperList)):
        # 获取论文名称
        paperName = paperList[i].find_element(by=By.CSS_SELECTOR, value=".name a").text
        
        # 获取作者列表
        authers = paperList[i].find_elements(by=By.CSS_SELECTOR, value=".author a")
        
        # 遍历每个作者
        for j in range(len(authers)):
            # 获取作者名称
            authorName = authers[j].text
            
            # 获取作者详情链接
            autherUrl = authers[j].get_attribute("href")
            
            # 如果作者详情链接无效，跳过
            if autherUrl == "javascript:void(0)":
                # updateAuthorData.update(authorName, "", {"paperList":paperName+";"})
                continue
            
            # 如果作者详情链接不是字符串，跳过
            if type(autherUrl) != str:
                continue
            
            # 访问作者详情页面
            driver.get(autherUrl)
            
            # 滚动页面到底部，确保所有内容加载完毕
            for _ in range(8):
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                time.sleep(1)
            
            # 初始化作者详细信息字典
            authorDetail = {}
            authorDetail["url"] = autherUrl
            
            # 获取作者所在单位和研究方向
            organize = driver.find_elements(by=By.CSS_SELECTOR, value="#kcms-author-info h3 span")
            if len(organize) > 0:
                if len(organize) > 1:
                    major = organize[1].text
                else:
                    major = ""
                organize = organize[0].text
                
                # 如果单位信息中包含分号，说明研究方向也在其中
                if organize.find(";") >= 0:
                    major = organize
                    organize = ""
            else:
                organize = ""
                major = ""
            
            # 存储作者的研究方向
            authorDetail["major"] = major
            
            # 获取发文量和下载量
            kl = driver.find_elements(by=By.CSS_SELECTOR, value="#kcms-author-info h5 .rowtit")
            vl = driver.find_elements(by=By.CSS_SELECTOR, value="#kcms-author-info h5 .amount")
            if(len(kl) == 0):
                # 如果没有找到发文量和下载量的相关元素
                print("异常：发文量和下载量匹配失败")
                errorOperate()
            for i in range(len(kl)):
                if kl[i].text == "总发文量：":
                    # 记录总发文量
                    authorDetail["paperCount"] = int(vl[i].text)
                elif kl[i].text == "总下载量：":
                    # 记录总下载量
                    authorDetail["downloadCount"] = int(vl[i].text)
                else:
                    # 如果存在未知参数
                    print("异常：存在未知参数: {}".format(kl[i]))
                    errorOperate()
            # 获取关键词
            keyword = driver.find_elements(by=By.CSS_SELECTOR, value="#keyword li a")
            authorDetail["aim"] = ""
            for e in keyword:
                # 将关键词拼接成字符串
                authorDetail["aim"] = authorDetail["aim"] + e.text + ";"
            # 获取论文
            selfPaper = driver.find_elements(by=By.CSS_SELECTOR, value="#KCMS-AUTHOR-CF li")
            authorDetail["paperList"] = []
            for i in range(len(selfPaper)):     # 作者文献
                nowPaperName = selfPaper[i].text
                if nowPaperName.rfind("\n") != -1:
                    nowPaperName = nowPaperName[0:nowPaperName.rfind("\n")]
                if nowPaperName.rfind("] ") != -1 and nowPaperName[0] == "[":
                    nowPaperName = nowPaperName[nowPaperName.rfind("] ")+2:len(nowPaperName)]
                if not nowPaperName in authorDetail["paperList"]:
                    # 添加论文名称到列表
                    authorDetail["paperList"].append(nowPaperName)
            selfPaper = driver.find_elements(by=By.CSS_SELECTOR, value="#KCMS-AUTHOR-DFR li")
            for i in range(len(selfPaper)):     # 最高下载
                nowPaperName = selfPaper[i].text
                if nowPaperName.rfind("\n") != -1:
                    nowPaperName = nowPaperName[0:nowPaperName.rfind("\n")]
                if nowPaperName.rfind("] ") != -1 and nowPaperName[0] == "[":
                    nowPaperName = nowPaperName[nowPaperName.rfind("] ")+2:len(nowPaperName)]
                if not nowPaperName in authorDetail["paperList"]:
                    # 添加论文名称到列表
                    authorDetail["paperList"].append(nowPaperName)
            selfPaper = driver.find_elements(by=By.CSS_SELECTOR, value="#KCMS-AUTHOR-JOURNAL-LITERATURES li")
            for i in range(len(selfPaper)):     # 发表在报纸的文献
                nowPaperName = selfPaper[i].text
                if nowPaperName.rfind("\n") != -1:
                    nowPaperName = nowPaperName[0:nowPaperName.rfind("\n")]
                if nowPaperName.rfind("] ") != -1 and nowPaperName[0] == "[":
                    nowPaperName = nowPaperName[nowPaperName.rfind("] ")+2:len(nowPaperName)]
                if not nowPaperName in authorDetail["paperList"]:
                    # 添加论文名称到列表
                    authorDetail["paperList"].append(nowPaperName)
            selfPaper = driver.find_elements(by=By.CSS_SELECTOR, value="#KCMS-AUTHOR-DISSERTATION-LITERATURES li")
            for i in range(len(selfPaper)):     # 发表在报纸的文献
                nowPaperName = selfPaper[i].text
                if nowPaperName.rfind("\n") != -1:
                    nowPaperName = nowPaperName[0:nowPaperName.rfind("\n")]
                if nowPaperName.rfind("] ") != -1 and nowPaperName[0] == "[":
                    nowPaperName = nowPaperName[nowPaperName.rfind("] ")+2:len(nowPaperName)]
                if not nowPaperName in authorDetail["paperList"]:
                    # 添加论文名称到列表
                    authorDetail["paperList"].append(nowPaperName)
            selfPaper = driver.find_elements(by=By.CSS_SELECTOR, value="#KCMS-AUTHOR-NEWSPAPER-LITERATURES li")
            for i in range(len(selfPaper)):     # 发表在报纸的文献
                nowPaperName = selfPaper[i].text
                if nowPaperName.rfind("\n") != -1:
                    nowPaperName = nowPaperName[0:nowPaperName.rfind("\n")]
                if nowPaperName.rfind("] ") != -1 and nowPaperName[0] == "[":
                    nowPaperName = nowPaperName[nowPaperName.rfind("] ")+2:len(nowPaperName)]
                if not nowPaperName in authorDetail["paperList"]:
                    # 添加论文名称到列表
                    authorDetail["paperList"].append(nowPaperName)
            # 格式化论文
            for i in range(len(authorDetail["paperList"])):
                # 替换分号为逗号
                authorDetail["paperList"][i] = authorDetail["paperList"][i].replace(";", ",")
            authorDetail["paperList"] = ";".join(authorDetail["paperList"])
            # 获取参考文献
            referPaper = driver.find_elements(by=By.CSS_SELECTOR, value="#KCMS-AUTHOR-REFERENCES-LITERATURES li")
            authorDetail["referPaper"] = []
            for i in range(len(referPaper)):
                nowPaperName = referPaper[i].text
                if nowPaperName.rfind("\n") != -1:
                    nowPaperName = nowPaperName[0:nowPaperName.rfind("\n")]
                if nowPaperName.rfind("] ") != -1 and nowPaperName[0] == "[":
                    nowPaperName = nowPaperName[nowPaperName.rfind("] ")+2:len(nowPaperName)]
                if not nowPaperName in authorDetail["referPaper"]:
                    # 添加参考文献名称到列表
                    authorDetail["referPaper"].append(nowPaperName)
            # 格式化论文
            for i in range(len(authorDetail["referPaper"])):
                # 替换分号为逗号
                authorDetail["referPaper"][i] = authorDetail["referPaper"][i].replace(";", ",")
            authorDetail["referPaper"] = ";".join(authorDetail["referPaper"])
            # 获取指导老师
            teacher = driver.find_elements(by=By.CSS_SELECTOR, value="#kcms-author-tutor li span")
            authorDetail["teacher"] = ""
            for e in teacher:
                # 拼接指导老师信息
                authorDetail["teacher"] = authorDetail["teacher"] + e.text + ";"
            if len(authorDetail["teacher"]) > 0 and authorDetail["teacher"][-1] == ";":
                # 去掉最后一个分号
                authorDetail["teacher"] = authorDetail["teacher"][0:-1]
            # 获取指导学生
            student = driver.find_elements(by=By.CSS_SELECTOR, value="#kcms-author-students #nodataText")
            if len(student) <= 0:
                student = driver.find_elements(by=By.CSS_SELECTOR, value="#kcms-author-students>*")
                if len(student) > 0:
                    # 如果有指导学生数据
                    print("继续：需要在此页面寻找指导学生数据")
                    errorOperate()
            # 获取支持基金会
            fund = driver.find_elements(by=By.CSS_SELECTOR, value="#kcms-author-fund-support li a")
            authorDetail["fund"] = []
            for i in range(len(fund)):
                if not fund[i].text in authorDetail["fund"]:
                    # 添加支持基金会名称到列表
                    authorDetail["fund"].append(fund[i].text)
            authorDetail["fund"] = ";".join(authorDetail["fund"])
            # 获取合作作者
            coopAut = driver.find_elements(by=By.CSS_SELECTOR, value="#kcms-author-cooperation li")
            authorDetail["cooperate"] = []
            for i in range(len(coopAut)):
                coopName = coopAut[i].find_elements(by=By.CSS_SELECTOR, value="b a")
                if len(coopName) > 0:
                    coopName = coopName[0].text
                    coopOrgan = coopAut[i].find_elements(by=By.CSS_SELECTOR, value="span a")
                    if len(coopOrgan) > 0:
                        coopOrgan = coopOrgan[0].text
                    else:
                        coopOrgan = ""
                    coop = coopName + "@" + coopOrgan
                    if not coop in authorDetail["cooperate"]:
                        # 添加合作作者信息到列表
                        authorDetail["cooperate"].append(coop)
            authorDetail["cooperate"] = ";".join(authorDetail["cooperate"])
            # 输出命令行，并保存到数据库
            # print(i,j,authorName,organize,major,paperName)
            # print(i+1, j+1, authorName, organize, authorDetail)
            # updateAuthorData.update(authorName, organize, authorDetail)
            driver.back()
            # cursor.execute("INSERT INTO author1 (name, organize, major, paperName) VALUES ('{}', '{}', '{}', '{}');".format(authorName, organize, major, paperName))
            # db.commit()
    if len(paperList) < 20:
        # 如果列表内容不满20条，提示检查是否已经结束
        print("\n\n\n注意: 列表内容不满, 请检查是否已经结束\n\n\n")
        break
    driver.find_element(by=By.CSS_SELECTOR, value="#PageNext").click()

# 结束
print("爬取结束")