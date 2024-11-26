# 导入csv模块，用于处理CSV文件
import csv
# 导入time模块，用于记录时间
import time

# 记录开始时间
k = time.time()

# 定义字段名
d = ['姓名', '组织', '关注领域', '论文', '合作作者', '引用次数', 'h指数', '引用次数', 'i10指数', '链接', '类型']
# 生成一些示例数据
d1 = range(11)
d2 = range(22, 33)
d3 = map(str, range(33, 44))

# 增加最大字段长度，防止处理大文件时出错
csv.field_size_limit(200000000)  # 根据实际情况调整数值

# 初始化一个空列表，用于存储字典数据
zxcv = []
# 添加示例数据到列表中
zxcv.append(dict(zip(d, d1)))
zxcv.append(dict(zip(d, d2)))
zxcv.append(dict(zip(d, d3)))
zxcv.append({'姓名': 123, '关注领域': '54，，，，，,,,,,66'})

# 打印字典数据
print(zxcv)
print()
print()
print()

# 字典形式写入CSV文件
with open("./test.csv", 'w', newline='', encoding='utf-8') as csvfile2:
    # 创建一个csv字典写入器
    csvfile2_writer = csv.DictWriter(csvfile2, fieldnames=d)
    # 写入字段名
    csvfile2_writer.writeheader()
    # 初始化一个空列表，用于存储已写入的姓名
    oook = []
    # 遍历字典数据
    for i in zxcv:
        # 如果当前姓名未写入过，则写入
        if i[d[0]] not in oook:
            csvfile2_writer.writerow(i)
            oook.append(i[d[0]])

# 读取CSV文件
with open(r"./test.csv", 'r', newline='', encoding='utf-8') as csvfile:
    # 创建一个csv阅读器
    csvreader = csv.reader(csvfile)
    # 读取所有行并转换为列表
    asd = list(csvreader)
    # 打印读取的数据
    print(asd)
    # for i in asd:
    #     print(i)

# 记录结束时间并打印用时
print("用时", time.time() - k, "秒")