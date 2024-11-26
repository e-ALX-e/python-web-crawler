# import csv

# extracted = [['标题', '时间', '来源', '作者', '正文', '文章链接', '图片']]

# # biaotou=dict(zip(['a', 'b', 'c', 'd', 'e', 'f', 'g'],['a', 'b', 'c', 'd', 'e', 'f', 'g']))
# # 将数据转换为字典形式
# obj = []
# for i in extracted:
#     obj.append(dict(zip(['a', 'b', 'c', 'd', 'e', 'f', 'g'], i)))
# obj.append({'a':456,'c':789,'g':123})


# # 写入CSV文件
# with open('.\\爬取的文档\\练习.csv', 'w', newline='', encoding='utf-8') as csvfile:
#     # 定义字段名
#     fieldnames = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#     csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
#     # # 写入表头
#     # csv_writer.writerows(biaotou)
#     csv_writer.writeheader()
    
#     # 写入数据
#     csv_writer.writerows(obj)
#     print(obj)

# "C:\code\python\爬取的文档\GPS论文第5部分.csv"
# import csv
# with open("C:\code\python\爬取的文档\GPS论文第5部分_清洗.csv", 'w', encoding='utf-8') as file_2:
#     # 定义字段名
#     # fieldnames = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#     # csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     csv_writer = csv.writer(file_2)
#     # # 写入表头
#     # csv_writer.writerows(biaotou)
#     csv_writer.writerow(['文章标题','文章链接','文章类型','文章日期','参与者','摘要','参考文献','资金','作者信息_单位','作者信息_贡献','作者信息_通信'])





import csv
asdf=5
# 打开CSV文件
with open(f"C:\code\python\爬取的文档\GPS论文第{asdf}部分.csv", 'r', encoding='utf-8') as file:
    # 创建csv阅读器
    reader = csv.reader(file)
    
    reader=list(reader)

    kkk=[]
    for j in reader[1:]:
        obj=[]
        for i in j:
            obj.append(''.join((i[2:-2]).split("', '")).replace('\\n','\n'))
        if obj:  # 确保非空列表才添加
            kkk.append(obj)
    num=0

# with open("C:\code\python\爬取的文档\GPS论文第5部分_清洗.csv", 'a', encoding='utf-8') as file_2:
#     # 定义字段名
#     csv_writer = csv.writer(file_2)
#     # # 写入表头
#     # fieldnames = ['文章标题', '文章链接', '文章类型', '文章日期', '参与者', '摘要', '参考文献', '资金', '作者信息_单位', '作者信息_贡献', '作者信息_通信']
#     # csv_writer.writeheader(fieldnames)
#     # 写入数据
#     csv_writer.writerows(kkk)
# print(kkk)




# import csv
# kkk=[[1,2,3,5],[1,5,9,8,44]]
# with open("C:\code\python\爬取的文档\GPS论文第5部分_清洗.csv", 'w', encoding='utf-8') as file_2:
#     # 定义字段名
#     csv_writer = csv.writer(file_2)
#     # # 写入表头
#     # fieldnames = ['文章标题', '文章链接', '文章类型', '文章日期', '参与者', '摘要', '参考文献', '资金', '作者信息_单位', '作者信息_贡献', '作者信息_通信']
#     # csv_writer.writeheader(fieldnames)
    
#     # 写入数据
#     csv_writer.writerows(kkk)
with open(f'C:\code\python\爬取的文档\GPS论文第{asdf}部分_清洗.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    # 写入表头
    csv_writer.writerow(['文章标题', '文章链接', '文章类型', '文章日期', '参与者', '摘要', '参考文献', '资金', '作者信息_单位', '作者信息_贡献', '作者信息_通信'])
    # 写入提取的数据
    csv_writer.writerows(kkk)