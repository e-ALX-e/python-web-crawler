# 导入csv模块，用于处理CSV文件
import csv  

# 读取第一个CSV文件
with open(r"Z:\新-清洗\维普网\合并后\全部数据_78.csv", 'r', newline='', encoding='utf-8') as csvfile:
    # 创建一个csv阅读器
    csvreader = csv.reader(csvfile)
    # 读取所有行并转换为列表
    asd = list(csvreader)  

# 初始化一个空列表，用于存储第一个文件中的标题
zxcv = []  
# 将每行的第一个元素（标题）添加到列表中
for i in asd:
    zxcv.append(i[0])  

# 读取第二个CSV文件
with open(r"Z:\新-清洗\知网\陈陈_21321321.csv", 'r', newline='', encoding='utf-8') as csvfile:
    # 创建一个csv阅读器
    csvreader = csv.reader(csvfile)
    # 读取所有行并转换为列表
    asdasd = list(csvreader)  

# 写入新的CSV文件
with open(r"Z:\新-清洗\知网\陈陈_21321321_489565465468569854968.csv", 'w', newline='', encoding='utf-8') as csvfile2:
    # 创建一个csv写入器
    writer = csv.writer(csvfile2)  
    # 写入字段名
    writer.writerow(['Title', 'Article_link', 'Authors', 'Abstract', 'Keywords', 'Source', 'Released', 'Area_of_Focus', 'Article_type', 'Data_type', 'Data', 'Institution'])
    # 遍历第二个文件中的每一行
    for i in asdasd:
        # 如果当前行的标题不在第一个文件的标题列表中
        if i[0] not in zxcv:
            # 写入当前行到新的CSV文件中
            writer.writerow(i)  