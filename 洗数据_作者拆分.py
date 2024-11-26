import csv
import time

k = time.time()

###############################
# 作者所在的序号
key = 2
# 作者用什么分割的
fuhao = ' '

###############################

# 打开原始CSV文件
with open("D:\桌面\国庆节数据清洗\卫星遥感期刊和论文_清洗02.csv", 'r', newline='', encoding='utf-8') as csvfile:
    # 创建一个csv阅读器
    csvreader = csv.reader(csvfile)
    # 将所有行读取为列表并去掉表头
    asd = list(csvreader)[1:]
    # # 逐行读取CSV文件
    # for row in csvreader:
    #     print(row)  # 打印每一行

# 定义表头
ziduanming = ['标题', 'url', '主要作者：', '其他作者：', '机构地区：', '出处：', '基金：', '摘要：', '关 键 词：', '分 类 号：']

# 打开新CSV文件以写入
with open("D:\桌面\国庆节数据清洗\卫星遥感期刊和论文_清洗03.csv", 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    # 写入表头
    csv_writer.writerow(ziduanming)
    # 写入提取的数据
    for i in asd:
        if len(i[key]):
            # 拆分作者字段
            sd = i[key].split(fuhao)
            # 列表去重
            sd = list(dict.fromkeys(sd))
            if len(sd) >= 2:
                # 如果作者数量大于等于2，将第一个作者作为主要作者，其余作者合并为其他作者
                sd = [sd[0], fuhao.join(sd[1:])]
            else:
                # 如果只有一个作者，其他作者为空
                sd = [sd[0], '']
            # 更新原列表中的作者信息
            i[key-1:key] = sd
            csv_writer.writerow(i)

# 打印清洗完成时间和耗时
print('清洗完成，耗时：', time.time() - k)