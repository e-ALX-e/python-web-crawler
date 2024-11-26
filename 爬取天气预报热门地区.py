# 导入requests库，用于发送HTTP请求
import requests
# 导入re模块，用于正则表达式匹配
import re

# 数据爬取
# 定义目标URL
url = 'http://www.weather.com.cn/weather1d/101310201.shtml'
# 发送GET请求获取数据
shuju = requests.get(url)
# 设置响应内容的编码为UTF-8
shuju.encoding = 'utf-8'

# 这条可以打印出爬取到的数据
# print(shuju.text)

# 数据处理
# 获取响应内容
wenben = shuju.text
# 使用正则表达式提取城市名称
name = re.findall('<span class="name">([\u4e00-\u9fa5]*)</span>', wenben)
# 使用正则表达式提取天气情况
weather = re.findall('<span class="weather">([\u4e00-\u9fa5]*)</span>', wenben)
# 使用正则表达式提取温度
wd = re.findall('<span class="wd">(.*)</span>', wenben)
# 使用正则表达式提取舒适度
zs = re.findall('<span class="zs">([\u4e00-\u9fa5]*)</span>', wenben)

# 创建一个空列表存储处理后的数据
s = []
# 使用zip函数将提取的数据组合在一起
rw = zip(name, weather, wd, zs)
# 遍历组合后的数据并添加到列表s中
for a, b, c, d in rw:
    s.append([a, b, c, d])

# 打印处理后的数据
print(s)
print()
print()

# 格式化输出数据
for i in s:
    for j in i:
        print(j, end='     \t')
    print()

'''
<span class="name">桂林</span>
<span class="weather">阴转多云</span>
<span class="wd">17/21℃</span>
<span class="zs">适宜</span>
'''