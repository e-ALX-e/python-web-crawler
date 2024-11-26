# 导入csv库，用于处理CSV文件
import csv  
# 导入time库，用于记录时间
import time  
# 导入re库，用于正则表达式操作
import re  

# 获取用户输入的文件地址
a = input("请输入文件的地址")
# 检查文件格式是否为.csv
if a[-4:] != '.csv':
    print('文件格式错误')
    exit()
else:
    print('文件格式正确')
    # 去掉文件扩展名
    文件地址 = a[:-4]  
    print(文件地址)

# 文件地址 = "D:\桌面\最终数据\合并后\合并"
# 定义文件后缀
后缀 = '第1次清洗.csv'

# 记录开始时间
ktime = time.time()  

# 定义字段名
字段名 = ['论文标题', '作者姓名', '作者单位', '作者通信', '发表日期', '链接', '摘要', '参考文献', '来源', '类型', '关键词', '研究领域']

# 关键词和错误关键词
关键词 = ['卫星', '遥感']
错误关键词 = ['细胞', '航天员']

# 打开并读取CSV文件
with open(文件地址 + '.csv', 'r', newline='', encoding='utf-8') as csvfile:
    # 创建一个csv阅读器
    csvreader = csv.reader(csvfile)
    # 跳过前两行
    asd = list(csvreader)[2:]  

# 示例数据
# '《遥感学报》北大核心CSCDEI'
# '发文量：被引量：0孙伟伟1发文量：被引量：0杨刚1发文量：被引量：0陈超2发文量：被引量：0常明会1+3位作者•'
# 存储处理后的数据
zxcv = []  
for i in asd:
    # 初始化临时字典
    临时字典 = {'论文标题': i[0], '链接': i[1], "作者通信": "", '参考文献': ""}  
    # 分割字符串
    alx = i[2].split('•')  
    # 更新类型
    临时字典.update({'类型': alx[0][1:-1]})  

    if len(alx) > 1:
        if '发文量' in alx[1]:
            # 定义正则表达式模式
            pattern = r'发文量|被引量|\d+|\+|：|,'  
            # 替换匹配项
            result = re.sub(pattern, ' ', alx[1])  
            # 分割字符串
            result = result.split(' ')  
            # 过滤空字符串
            filtered_list = [item for item in result if item != '']  
            # 用逗号连接
            filtered_list = '，'.join(filtered_list)  
            # 更新作者姓名
            临时字典.update({'作者姓名': filtered_list})  

    for j in alx:
        if '年' in j:
            # 更新发表日期
            临时字典.update({'发表日期': j[:4]})  

        if "》" in j and "《" in j:
            # 查找期刊名称
            result = re.findall(r'《.*?》', j)  
            # 更新来源
            临时字典.update({'来源': result[0]})  

    for j in i:
        if '机构： ' in j:
            # 去除前缀
            text = j.replace("机构： ", "")  
            # 分割字符串
            parts = re.split(r'\[(\d+)\]', text)  
            # 去除空格
            parts = [part.strip() for part in parts if part.strip()]  
            # 过滤数字
            filtered_list = [item for item in parts if not item.isdigit()]  
            # 用逗号连接
            filtered_list = '，'.join(filtered_list)  
            # 更新作者单位
            临时字典.update({'作者单位': filtered_list})  

        if '摘要： ' in j:
            # 去除前缀
            text = j.replace("摘要： ", "")  
            # 更新摘要
            临时字典.update({'摘要': text})  

        if '关键词: ' in j:
            # 去除前缀
            text = j.replace("关键词: ", "")  
            # 分割字符串
            parts = text.split(' ；')  
            # 用分号连接
            text = ' ；'.join(parts)  
            # 更新关键词
            临时字典.update({'关键词': text})  

        if '研究领域：' in j:
            # 去除前缀
            text = j.replace("研究领域：", "")  
            # 更新研究领域
            临时字典.update({'研究领域': text})  

    # 将临时字典添加到列表中
    zxcv.append(临时字典)  

# 写入新的CSV文件
with open(文件地址 + 后缀, 'w', newline='', encoding='utf-8') as csvfile2:
    # 普通写入
    # csvfile2_writer = csv.writer(csvfile2)
    # csvfile2_writer.writerows(zxcv)
    
    # 创建一个csv字典写入器
    csvfile2_writer = csv.DictWriter(csvfile2, fieldnames=字段名)
    # 写入表头
    csvfile2_writer.writeheader()  
    # 用于记录已写入的论文标题
    oook = []  
    for i in zxcv:
        if i[字段名[0]] not in oook:
            # 写入行
            csvfile2_writer.writerow(i)  
            # 记录已写入的论文标题
            oook.append(i[字段名[0]])  

# 输出运行时间
print(time.time() - ktime)  
