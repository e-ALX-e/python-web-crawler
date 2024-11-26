# 导入csv模块，用于处理CSV文件
import csv
# 导入time模块，用于记录时间
import time
# 导入re模块，用于正则表达式操作
import re

# 用户输入文件的地址
a = input("清输入文件的地址")[1:-1]
# 检查文件格式是否为.csv
if a[-4:] != '.csv':
    print('文件格式错误')
    print(a[:-4])
    exit()
else:
    print('文件格式正确')
    # 去掉文件扩展名，获取文件地址
    文件地址 = a[:-4]
    print(文件地址)
    
# 示例文件地址
# 文件地址 = "D:\桌面\最终数据\合并后\合并"
# 合并后的文件后缀
后缀 = '第1次清洗.csv'

# 记录开始时间
ktime = time.time()

# 定义字段名
字段名 = ['论文标题', '作者姓名', '作者单位', '作者通信', '发表日期', '链接', '摘要', '参考文献', '来源', '类型', '关键词', '研究领域']

# 关键词列表
关键词 = ['卫星', '遥感']
# 错误关键词列表
错误关键词 = ['细胞', '航天员']

# 打开原始CSV文件
with open(文件地址 + '.csv', 'r', newline='', encoding='utf-8') as csvfile:
    # 创建一个csv阅读器
    csvreader = csv.reader(csvfile)
    # 跳过前两行
    asd = list(csvreader)[2:]

# 示例数据
'《遥感学报》北大核心CSCDEI'
'发文量：被引量：0孙伟伟1发文量：被引量：0杨刚1发文量：被引量：0陈超2发文量：被引量：0常明会1+3位作者•'
# 初始化结果列表
zxcv = []
# 遍历每行数据
for i in asd:
    # 初始化临时字典
    临时字典 = {'论文标题': i[0], '链接': i[1], "作者通信": '', '参考文献': ''}
    # 分割作者信息
    alx = i[2].split('•')
    # 更新类型字段
    临时字典.update({'类型': alx[0][1:-1]})
    # 处理作者信息
    if len(alx) > 1:
        if '发文量' in alx[1]:
            pattern = r'发文量|被引量|\d+|\+|：|,'
            result = re.sub(pattern, ' ', alx[1])
            result = result.split(' ')
            filtered_list = [item for item in result if item != '']
            filtered_list = '，'.join(filtered_list)
            临时字典.update({'作者姓名': filtered_list})
    # 处理其他字段
    for j in alx:
        if '年' in j:
            临时字典.update({'发表日期': j[:4]})
        if "》" in j and "《" in j:
            result = re.findall(r'《.*?》', j)
            临时字典.update({'来源': result[0]})
    for j in i:
        if '机构：' in j:
            text = j.replace("机构：", "")
            parts = re.split(r'\[(\d+)\]', text)
            parts = [part.strip() for part in parts if part.strip()]
            filtered_list = [item for item in parts if not item.isdigit()]
            filtered_list = '，'.join(filtered_list)
            临时字典.update({'作者单位': filtered_list})
        if '摘要：' in j:
            text = j.replace("摘要：", "")
            临时字典.update({'摘要': text})
        if '关键词:' in j:
            text = j.replace("关键词:", "")
            parts = text.split(' ；')
            text = ' ；'.join(parts)
            临时字典.update({'关键词': text})
        elif '关键词：' in j:
            text = j.replace("关键词：", "")
            parts = text.split(' ；')
            text = ' ；'.join(parts)
            临时字典.update({'关键词': text})
        if '研究领域：' in j:
            text = j.replace("研究领域：", "")
            临时字典.update({'研究领域': text})
    # 将临时字典添加到结果列表
    zxcv.append(临时字典)

# 写入清洗后的数据到新的CSV文件
with open(文件地址 + 后缀, 'w', newline='', encoding='utf-8') as csvfile2:
    # 创建字典写入器
    csvfile2_writer = csv.DictWriter(csvfile2, fieldnames=字段名)
    # 写入表头
    csvfile2_writer.writeheader()
    oook = []
    # 写入数据行，去重
    for i in zxcv:
        if i[字段名[0]] not in oook:
            csvfile2_writer.writerow(i)
            oook.append(i[字段名[0]])

# 打印清洗完成时间和用时
print('清洗完成，用时', time.time() - ktime, '秒')