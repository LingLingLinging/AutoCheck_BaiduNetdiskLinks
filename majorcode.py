import re  # 导入正则表达式模块
import os  # 导入操作系统模块
from selenium import webdriver  # 导入selenium模块中的webdriver类

# 读取txt文件内容=======================
def read_txt_file(file_path):
    file_size = os.path.getsize(file_path)
    if file_size < 10 * 1024 * 1024:  # 如果文件小于10MB
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    else:  # 如果文件大于等于10MB
        content = []
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                content.append(line)
        content = ''.join(content)
    return content

# 输入文件路径
file_path = input()

# 古怪路径格式处理=======================
# 去除首尾的引号
if file_path[0] == '"':
    file_path = file_path[1:]
if file_path[-1] == '"':
    file_path = file_path[:-1]
# 将反斜杠替换为正斜杠
file_path = re.sub(r'\\', '/', file_path)

file_content = read_txt_file(file_path)

# 使用正则表达式查找匹配的内容，使用非捕获组以匹配整个链接
pattern = r'https://pan.baidu.com/s/[a-zA-Z0-9_-]+(?:\?pwd=[a-zA-Z0-9]{4})?'
matches = re.findall(pattern, file_content)

# 只输出匹配上的整个链接
for match in matches:
    print(match)