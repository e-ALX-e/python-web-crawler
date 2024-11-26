# 导入csv模块，用于处理CSV文件
import csv  
# 导入time模块，用于计算程序运行时间
import time  

# 记录程序开始时间
k = time.time()  

# 定义原始字段名列表
字段名 = ['Title', 'Article_link', 'Authors', 'Abstract', 'Keywords', 'Source', 'Released', 'Area_of_Focus', 'Article_type', 'Data_type', 'Data', 'Institution']  
# 定义字段名副本列表
字段名副本 = ['论文标题', '作者姓名', '作者单位', '作者通信', '发表日期', '链接', '摘要', '参考文献', '来源', '类型', '关键词', '研究领域']  
# 定义另一个字段名列表，包含重复项
字段名2 = ['Title', 'Authors', '123', '123', 'Released', 'Article_link', 'Abstract', '123', 'Source', 'Article_type', 'Keywords', 'Area_of_Focus', 'Institution']  

# 打印字段名列表
print(字段名)  

# 打开CSV文件
with open(r"Z:\新-清洗\知网\陈陈.csv", 'r', newline='', encoding='utf-8') as csvfile:  
    # 创建一个csv阅读器
    csvreader = csv.reader(csvfile)
    # 跳过表头，读取所有数据行
    asd = list(csvreader)[1:]  

# 初始化一个空列表，用于存储处理后的数据
zxcv = []  
# 遍历每一行数据
for i in asd:  
    # 将字段名与数据行对应，生成字典
    ling = dict(zip(字段名2, i))  
    # 添加额外的键值对
    ling.update({'Data_type': 'Artical', 'Data': 'Data'})  
    # 删除多余的键
    del ling['123']  
    # 这行代码无效，已注释掉
    # ling.clear('123')  
    # 将处理后的字典添加到列表中
    zxcv.append(ling)  

# 打印前10条处理后的数据（已注释）
# print(zxcv[:10])  

# 打开新的CSV文件，准备写入
with open(r"Z:\新-清洗\知网\陈陈_21321321.csv", 'w', newline='', encoding='utf-8') as csvfile2:  
    # 创建一个字典写入器
    csvfile2_writer = csv.DictWriter(csvfile2, fieldnames=字段名)  
    # 写入字段名
    csvfile2_writer.writeheader()  
    # 初始化一个空列表，用于记录已写入的标题
    oook = []  
    # 遍历处理后的数据
    for i in zxcv:  
        # 如果标题未被写入
        if i[字段名2[0]] not in oook:  
            # 写入当前数据行
            csvfile2_writer.writerow(i)  
            # 记录已写入的标题
            oook.append(i[字段名2[0]])  

# 打印程序运行时间
print(time.time() - k)  