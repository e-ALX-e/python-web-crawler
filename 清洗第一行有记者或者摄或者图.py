# "D:\文档\WeChat Files\wxid_rz1yjqpifm2822\FileStorage\File\2024-10\公司.csv"
# 导入csv模块，用于处理CSV文件
import csv
# 导入time模块，用于时间相关的操作
import time

# 打开原始CSV文件
with open(r"D:\文档\WeChat Files\wxid_rz1yjqpifm2822\FileStorage\File\2024-10\公司.csv", 'r', newline='', encoding='utf-8') as csvfile:
    # 创建一个csv阅读器
    csvreader = csv.reader(csvfile)
    # 读取所有行并转换为列表
    biaoti = list(csvreader)
    # 提取第二行及以后的数据
    asd = biaoti[1:]
    # 提取表头
    biaoti = biaoti[0]

# 创建一个空列表用于存储处理后的数据
zxcv = []
# 遍历每一行数据
for i in asd:
    # 获取第二列的文本
    text = i[1]
    # 检查文本中是否包含“摄”、“记者”或“图”
    if '摄' in text or '记者' in text or '图':
        # 将文本按换行符分割
        j = text.split('\n')
        # 去除第一行并重新组合文本
        i[1] = ''.join(j[1:])
    # 将处理后的数据转换为字典并添加到列表中
    zxcv.append(dict(zip(biaoti, i)))

# 打开新的CSV文件，用于写入处理后的数据
with open("D:\桌面\公司123121323.csv", 'w', newline='', encoding='utf-8') as csvfile2:
    # 创建一个csv写入器
    csvfile2_writer = csv.DictWriter(csvfile2, fieldnames=biaoti)
    # 写入表头
    csvfile2_writer.writeheader()
    # 遍历处理后的数据并写入文件
    for i in zxcv:
        csvfile2_writer.writerow(i)