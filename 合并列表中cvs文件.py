import os
import csv
a=input("清输入文件的文件夹位置")
directory=a
output_file=a+input("请输入合并后文件的名字")
# directory = 'D:\桌面\最终数据'  # 替换为你的CSV文件所在的目录
# output_file = 'D:\桌面\最终数据\合并后\合并.csv'  # 替换为你希望保存合并后文件的名称




def merge_csv_files(directory, output_file):
    """
    合并指定目录下的所有CSV文件到一个输出文件中。
    
    :param directory: 包含CSV文件的目录路径
    :param output_file: 输出合并后的CSV文件的路径
    """
    # 获取目录下所有csv文件的列表
    csv_files = [file for file in os.listdir(directory) if file.endswith('.csv')]
    
    # 打开输出文件
    with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        
        # 标记是否已经写入了表头
        header_written = False
        
        # 遍历每个csv文件
        for file in csv_files:
            file_path = os.path.join(directory, file)
            
            with open(file_path, 'r', newline='', encoding='utf-8') as infile:
                reader = csv.reader(infile)
                
                # 读取表头
                headers = next(reader)
                
                # 写入表头（仅第一次）
                if not header_written:
                    writer.writerow(headers)
                    header_written = True
                
                # 写入数据行
                for row in reader:
                    writer.writerow(row)

# 使用示例

merge_csv_files(directory, output_file)