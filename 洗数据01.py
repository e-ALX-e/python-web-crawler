# # C:\code\python\爬取的文档\GPS论文第1部分.csv

# with open('C:\code\python\爬取的文档\GPS论文第1部分.csv', 'w', newline='', encoding='utf-8') as csvfile:
#     csv_writer = csv.writer(csvfile)
#     # 写入表头
#     csv_writer.writerow(['标题', '时间','来源','作者','正文','文章链接','图片'])
#     # 写入提取的数据
#     csv_writer.writerows(extracted_data_2)
    
# with open('.\\爬取的文档\\数据清洗_GPS.csv', 'r', newline='', encoding='utf-8') as csvfile:
#     # 创建一个csv阅读器
#     csvreader = csv.reader(csvfile)
#     print(list(csvreader))
#     # 逐行读取CSV文件
#     for row in csvreader:
#         print(row)  # 打印每一行
