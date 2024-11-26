# 文件路径
# C:\code\python\爬取的文档\卫星遥感期刊和论文.csv
import csv

# 定义字段名
fieldnames = ['标题', 'url', '作　　者：', '机构地区：', '出　　处：', '基　　金：', '摘　　要：', '关 键 词：', '分 类 号：']

# 存储原始数据
patents = []

# 打开原始CSV文件
with open('C:\code\python\爬取的文档\卫星遥感期刊和论文.csv', 'r', newline='', encoding='utf-8') as csvfile:
    # 创建一个csv阅读器
    csvreader = csv.reader(csvfile)
    # 将所有行读取为列表
    patents = list(csvreader)

# 存储清洗后的数据
patents_2 = []
for i in patents:
    # 创建一个字典来存储每条记录
    lis_pat = {}
    for j in range(len(i)):
        # 检查当前元素是否在字段名列表中
        if i[j] in fieldnames:
            # 检查下一个元素是否存在且不是字段名
            if j + 1 <= len(i) and i[j + 1] not in fieldnames:
                # 创建键值对并更新字典
                dict = {i[j]: i[j + 1]}
                lis_pat.update(dict)
    # 将字典添加到清洗后的数据列表中
    patents_2.append(lis_pat)

# 打开新CSV文件以写入
with open("D:\桌面\国庆节数据清洗\卫星遥感期刊和论文_清洗.csv", 'w', encoding='utf-8') as file_2:
    # 创建一个csv字典写入器
    writer = csv.DictWriter(file_2, fieldnames=fieldnames)
    # 写入表头
    writer.writeheader()
    # 写入清洗后的数据
    for patent in patents_2:
        writer.writerow(patent)

# 打印完成信息
print('ok')
# 打印清洗后的数据
# print(patents_2)