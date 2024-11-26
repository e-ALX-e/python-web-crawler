# 文件路径
# "D:\桌面\工作簿2.csv"
import csv

# 原始数据列表
# asd=[国家,企业名,企业名缩写,成立时间,公司地点,专题,隶属,子公司,主要领导,领域,内容标题,内容时间,内容,href]
# 需要去重的列索引
# 10

# 打开原始CSV文件
with open("D:\桌面\工作簿2.csv", 'r', newline='', encoding='utf-8') as csvfile:
    # 创建一个csv阅读器
    csvreader = csv.reader(csvfile)
    # 将所有行读取为列表
    asd = list(csvreader)
    # # 逐行读取CSV文件
    # for row in csvreader:
    #     print(row)  # 打印每一行

# 打开新CSV文件以写入
with open("D:\桌面\工作簿_清洗.csv", 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    # 写入表头
    csv_writer.writerow(['国家', '企业名', '企业名缩写', '成立时间', '公司地点', '专题', '隶属', '子公司', '主要领导', '领域', '内容标题', '内容时间', '内容'])
    # 写入提取的数据

    oook = []
    for i in asd:
        # 检查当前行的第11列（索引10）是否已存在于oook中
        if i[10] not in oook:
            # 如果不存在，则添加到oook中并写入新CSV文件
            oook.append(i[10])
            csv_writer.writerow(i[:-1])