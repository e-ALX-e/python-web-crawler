# 导入csv模块，用于处理CSV文件
import csv  
# 导入time模块，用于计算程序运行时间
import time  

# 记录程序开始时间
k = time.time()  

# 定义CSV文件的列名
d = ['姓名', '组织', '关注领域', '论文', '合作作者', '引用次数', 'h指数', '引用次数', 'i10指数', '链接', '类型']  

# 增加最大字段长度，防止读取大字段时出错
csv.field_size_limit(200000000)  # 根据实际情况调整数值

# 打开原始CSV文件
with open(r"D:\桌面\Google作者数据011111.csv", 'r', newline='', encoding='utf-8') as csvfile:
    # 创建一个csv阅读器
    csvreader = csv.reader(csvfile)
    # 将CSV文件内容读取为列表
    asd = list(csvreader)  

# 初始化一个空列表，用于存储字典形式的数据
zxcv = []  
for i in asd:
    # 将每行数据转换为字典并添加到列表中
    zxcv.append(dict(zip(d, i)))  

# 字典形式写入新的CSV文件
with open("D:\桌面\Google作者数据222222222.csv", 'w', newline='', encoding='utf-8') as csvfile2:
    # 创建一个字典写入器
    csvfile2_writer = csv.DictWriter(csvfile2, fieldnames=d)  
    # 初始化一个空列表，用于存储已处理的姓名
    oook = []  
    for i in zxcv:
        # 检查姓名是否已处理过
        if i[d[0]] not in oook:  
            # 写入未处理过的数据
            csvfile2_writer.writerow(i)  
            # 将已处理的姓名添加到列表中
            oook.append(i[d[0]])  

# 打印程序运行时间
print(time.time() - k)  