import csv
import time

# 获取用户输入的文件地址
a = input("清输入文件的地址，和上一个地址一样")
# 检查文件格式是否正确
if a[-4:] != '.csv':
    print('文件格式错误')
    exit()
else:
    print('文件格式正确')
    文件地址 = a[:-4]
    print(文件地址)
# 文件地址 = "D:\桌面\最终数据\合并后\合并"
后缀 = '____查重校验后.csv'

# 记录开始时间
ktime = time.time()

# 定义字段名
d = ['Title', 'Article_link', 'Authors', 'Abstract', 'Keywords', 'Source', 'Released', 'Area_of_Focus', 'Article_type', 'Data_type', 'Data', 'Institution', 'Author unit']
字段名 = ['论文标题', '作者姓名', '作者单位', '作者通信', '发表日期', '链接', '摘要', '参考文献', '来源', '类型', '关键词', '研究领域']
关键词 = ['卫星', '遥感', '航天', '火箭', '空间']
错误关键词 = ['细胞', ' 航天邮', '八爪鱼', '基因', '细胞壁']

# 打开原始CSV文件
with open(文件地址 + '第1次清洗' + '.csv', 'r', newline='', encoding='utf-8') as csvfile:
    # 创建一个csv阅读器
    csvreader = csv.reader(csvfile)
    asd = list(csvreader)
    print(asd[0])  # 打印表头

# with open("D:\桌面\Google作者数据01.csv", 'w', newline='', encoding='utf-8') as csvfile2:
#     csvfile2_writer = csv.writer(csvfile2)

# 过滤符合条件的数据
zxcv = []
for i in asd:
    for j in 关键词:
        biaozhi = 1
        if j in i[0]:
            biaozhi = 0
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
        if biaozhi == 0:
            zxcv.append(i)
            break

# 写入过滤后的数据到新CSV文件
with open(文件地址 + '第1次清洗' + 后缀, 'w', newline='', encoding='utf-8') as csvfile2:
    字段名 = [asd[0]]
    csvfile2_writer = csv.writer(csvfile2)
    csvfile2_writer.writerows(字段名)
    csvfile2_writer.writerows(zxcv)

#     csvfile2_writer = csv.DictWriter(csvfile2, fieldnames=d)
#     # csvfile2_writer.writeheader()
#     oook = []
#     for i in zxcv:
#         if i[d[0]] not in oook:
#             csvfile2_writer.writerow(i)
#             oook.append(i[d[0]])

# 打印执行时间
print(time.time() - ktime)