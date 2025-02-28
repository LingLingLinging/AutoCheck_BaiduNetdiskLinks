import re  # 导入正则表达式模块
import os  # 导入操作系统模块
import requests  # 导入 requests 模块
import time  # 导入时间模块

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

# 读取csv文件内容=======================
def read_csv_file(file_path):
    import csv
    content = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            content.append(','.join(row))
    return '\n'.join(content)

# 读取markdown文件内容=======================
def read_md_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

# 检查百度网盘链接=======================
def check(url):
    """
    使用 requests 访问指定 URL，并检查页面中是否包含“请输入提取码”。
    """
    # 定义请求头，模拟浏览器访问（有时需要额外的 Cookie 等信息）
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        "Cache-Control": "no-cache",
        "Pragma": "no-cache"
    }
    
    # 发送 GET 请求
    response = requests.get(url, headers=headers)
    
    # 检查响应状态码
    if response.status_code == 200:
        # 获取页面内容
        content = response.text
        # 使用正则表达式匹配“请输入提取码”
        if re.search(r"请输入提取码", content):
            return True
        else:
            return False
    elif response.status_code == 404:
        return 404
    else:
        return "Error: " + str(response.status_code)

# 输入文件路径
file_path = input("请输入文件路径: ")

# 古怪路径格式处理=======================
# 去除首尾的引号
if file_path[0] == '"':
    file_path = file_path[1:]
if file_path[-1] == '"':
    file_path = file_path[:-1]
# 将反斜杠替换为正斜杠
file_path = re.sub(r'\\', '/', file_path)

# 根据文件类型读取文件内容=======================
file_extension = os.path.splitext(file_path)[1].lower()
if file_extension == '.txt':
    file_content = read_txt_file(file_path)
elif file_extension == '.csv':
    file_content = read_csv_file(file_path)
elif file_extension == '.md':
    file_content = read_md_file(file_path)
else:
    print("Unsupported file type")
    exit()

# 使用正则表达式查找匹配的内容，使用非捕获组以匹配整个链接
pattern = r'https://pan.baidu.com/s/[a-zA-Z0-9_-]+(?:\?pwd=[a-zA-Z0-9]{4})?'
matches = re.findall(pattern, file_content)

# 运行中
print("...............running...............")
# 只输出匹配上的整个链接
for match in matches:
    # 记录开始时间
    start_time = time.time()
    
    flag = check(match)
    
    # 记录结束时间
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    if flag == True:
        print(f"【++++++++++++++++++】\n\tFind:Available online: {match} \n(Time taken: {elapsed_time:.2f} seconds)")
    elif flag == False:
        print(f"【------------------】\n\tFind:Unavailable link: {match} \n(Time taken: {elapsed_time:.2f} seconds)")
    elif flag == 404:
        print(f"【404404404404404404】\n\tNo such file in link : {match} \n(Time taken: {elapsed_time:.2f} seconds)")
    else:
        print(flag)