# 导入csv模块，用于处理CSV文件
import csv
# 导入time模块，用于记录时间
import time

# 用户输入文件的地址
a = input("清输入文件的地址，和上一个地址一样")[1:-1]
# 检查文件格式是否为.csv
if a[-4:] != '.csv':
    print('文件格式错误')
    exit()
else:
    print('文件格式正确')
    # 去掉文件扩展名，获取文件地址
    文件地址 = a[:-4]
    print(文件地址)

# 示例文件地址
# 文件地址 = "D:\桌面\最终数据\合并后\合并"
# 合并后的文件后缀
后缀 = '____查重校验后.csv'

# 记录开始时间
ktime = time.time()

# 定义字段名
d = ['Title', 'Article_link', 'Authors', 'Abstract', 'Keywords', 'Source', 'Released', 'Area_of_Focus', 'Article_type', 'Data_type', 'Data', 'Institution', 'Author unit']
字段名 = ['论文标题', '作者姓名', '作者单位', '作者通信', '发表日期', '链接', '摘要', '参考文献', '来源', '类型', '关键词', '研究领域']

# 关键词列表
关键词 = ['卫星', '遥感', '航天', '火箭', '空间', '航空发动机']
# 错误关键词列表
错误关键词 = ['细胞', ' 航天邮', '八爪鱼', '基因', '细胞壁']

# 打开原始CSV文件
with open(文件地址 + '第1次清洗' + '.csv', 'r', newline='', encoding='utf-8') as csvfile:
    # 创建一个csv阅读器
    csvreader = csv.reader(csvfile)
    # 读取所有行
    asd = list(csvreader)
    print(asd[0])

# 初始化结果列表
zxcv = []
# 遍历每行数据
for i in asd:
    # 遍历关键词
    for j in 关键词:
        biaozhi = 1
        # 检查论文标题是否包含关键词
        if j in i[0]:
            biaozhi = 0
            # 检查论文标题、摘要、关键词是否包含错误关键词
            for k in 错误关键词:
                if k in i[0] or k in i[3] or k in i[6]:
                    biaozhi = 1
                    break
        # if j in i[3]:
        #     biaozhi = 0
        #     for k in 错误关键词:
        #         if k in i[0] or k in i[3]:
        #             biaozhi = 1
        #             break
        # 如果包含关键词且不包含错误关键词，将数据添加到结果列表
        if biaozhi == 0:
            zxcv.append(i)
            break

# 写入清洗后的数据到新的CSV文件
with open(文件地址 + '第1次清洗' + 后缀, 'w', newline='', encoding='utf-8') as csvfile2:
    # 定义字段名
    字段名 = [asd[0]]
    # 创建csv写入器
    csvfile2_writer = csv.writer(csvfile2)
    # 写入表头
    csvfile2_writer.writerows(字段名)
    # 写入数据行
    csvfile2_writer.writerows(zxcv)

#     csvfile2_writer = csv.DictWriter(csvfile2, fieldnames=d)
#     # csvfile2_writer.writeheader()
#     oook = []
#     for i in zxcv:
#         if i[d[0]] not in oook:
#             csvfile2_writer.writerow(i)
#             oook.append(i[d[0]])
# 打印清洗完成时间和用时
print(time.time() - ktime)