import csv
import time

k = time.time()
# "D:\桌面\工作簿2.csv"
# asd=[国家,企业名,企业名缩写,成立时间,公司地点,专题,隶属,子公司,主要领导,领域,内容标题,内容时间,内容,href]
# 10
# D:\桌面\国庆节数据清洗\卫星遥感期刊和论文_清洗.csv

###############################
# 对几号元素查重
key = 6

###############################

# 打开原始CSV文件
with open("D:\桌面\国庆节数据清洗\卫星遥感期刊和论文_清洗.csv", 'r', newline='', encoding='utf-8') as csvfile:
    # 创建一个csv阅读器
    csvreader = csv.reader(csvfile)
    # 将所有行读取为列表并去掉表头
    asd = list(csvreader)[1:]
    # # 逐行读取CSV文件
    # for row in csvreader:
    #     print(row)  # 打印每一行

# 定义表头
ziduanming = ['标题', 'url', '作　　者：', '机构地区：', '出　　处：', '基　　金：', '摘　　要：', '关 键 词：', '分 类 号：']

# 打开新CSV文件以写入
with open("D:\桌面\国庆节数据清洗\卫星遥感期刊和论文_清洗02.csv", 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    # 写入表头
    csv_writer.writerow(ziduanming)
    # 写入提取的数据
    oook = []
    for i in asd:
        if i[key] not in oook:
            oook.append(i[key])
            csv_writer.writerow(i)

# 打印清洗完成时间和耗时
print('清洗完成，耗时：', time.time() - k)