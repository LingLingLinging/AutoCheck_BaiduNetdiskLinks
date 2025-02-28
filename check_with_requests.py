import requests
import re

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
        #print(content)  # 如果需要可以去掉
        # 使用正则表达式匹配“请输入提取码”
        if re.search(r"请输入提取码", content):
            return True
        else:
            return False
    else:
        return "Error: " + str(response.status_code)