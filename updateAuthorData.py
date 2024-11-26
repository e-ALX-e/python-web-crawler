import MySQLdb

class UpdateAuthorData:
    def __init__(self):
        # 连接数据库
        # self.db = MySQLdb.connect("localhost", "root", "dMG6u-jZD#-6", "cnkidata", charset='utf8')
        # self.cursor = self.db.cursor()
        
        # 初始化存储作者信息的字典
        self.get = {}
        
        # 读取数据文件并解析
        with open('data.csv', 'r', encoding="utf-8") as file: 
            line = file.readline() 
            while line: 
                if line.find(",") != -1:
                    # 提取作者姓名
                    name = line[1:line.find(",")-1]
                    line = line[line.find(",")+1:len(line)]
                    if line.find(",") != -1:
                        # 提取作者单位
                        org = line[1:line.find(",")-1]
                        # 将作者信息存入字典
                        self.get["{}@{}".format(name, org)] = True
                line = file.readline()

    def update(self, name, organize, other):
        # 数据检查
        other["name"] = name
        other["organize"] = organize
        
        # 检查并设置默认值
        if not ("major" in other):
            other["major"] = ""
        if not ("aim" in other):
            other["aim"] = ""
        if not ("paperList" in other):
            other["paperList"] = ""
        if not ("referPaper" in other):
            other["referPaper"] = ""
        if not ("teacher" in other):
            other["teacher"] = ""
        if not ("student" in other):
            other["student"] = ""
        if not ("cooperate" in other):
            other["cooperate"] = ""
        if not ("fund" in other):
            other["fund"] = ""
        if not ("nationality" in other):
            other["nationality"] = ""
        if not ("url" in other):
            other["url"] = ""
        if not ("paperCount" in other):
            other["paperCount"] = 0
        if not ("downloadCount" in other):
            other["downloadCount"] = 0
        
        # 构建新的数据行
        newDataLine = '"{}","{}","{}","{}","{}","{}","{}","{}","{}","{}",{},{},"{}"\n'.format(
            other["name"], other["organize"], other["aim"],
            other["paperList"], other["referPaper"], other["teacher"],
            other["student"], other["cooperate"], other["fund"],
            other["nationality"], other["paperCount"], other["downloadCount"],
            other["url"])
        
        # 检查是否已存在该作者信息
        if "{}@{}".format(other["name"],other["organize"]) not in self.get:
            self.get["{}@{}".format(other["name"],other["organize"])] = True
            print(newDataLine)
            # 将新数据行写入文件
            with open('data.csv', 'a', encoding="utf-8") as f:
                f.write(newDataLine)
        else:
            print("已重复","{}@{}".format(other["name"],other["organize"]))