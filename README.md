# AutoCheck_BaiduNetdiskLinks

Auto check links in texts to make sure they are available.  
Originally used for the nbu-icicles project.

## Overview:
- A preliminary script initially developed for the nbu-icicles project, used to verify whether links in files (webpages) have expired.
- The current development goal is to implement automatic checking of Baidu Netdisk links.
- In the future, it will support OneDrive, Quark, Xunlei, and other cloud storage services.

## Supported File Formats:
- `.txt` (Text files)
- `.csv` (Comma-separated values files)
- `.md` (Markdown files)

## Requirements:
- Python 3.6 or higher
- Requests library (`pip install requests`)

## Usage:
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/AutoCheck_BaiduNetdiskLinks.git
   cd AutoCheck_BaiduNetdiskLinks
    ```
2. Install the required dependencies:
   ```bash
    pip install -r requirements.txt
   ```
3. Run the script:
   ```bash
   python totalcode.py
   ```
4. Enter the file path when prompted:
   ```bash
   Please enter the file path: "C:/path/to/your/file.txt"
   ```
5.  The script will check the links in the file and output the results.

## Current Status:
I am currently meeting the preliminary requirements of the nbu-icicles project. In the future, I plan to expand the supported file types and implement features such as automatic folder traversal.



---
### 中文版


# AutoCheck_BaiduNetdiskLinks

## 简述：
- 一个初步为 nbu-icicles 项目开发的脚本，用于确认文件（网页）中的链接是否过期。
- 当前开发目标为实现自动检查百度网盘链接。
- 将来会支持 OneDrive、夸克、迅雷等网盘。

## 支持的文件格式：
- `.txt`（文本文件）
- `.csv`（逗号分隔值文件）
- `.md`（Markdown 文件）

## 需求：
- Python 3.6 或更高版本
- Requests 库（`pip install requests`）

## 使用方法：
1. 克隆仓库：
   ```bash
   git clone https://github.com/yourusername/AutoCheck_BaiduNetdiskLinks.git
   cd AutoCheck_BaiduNetdiskLinks 
   ```
2. 安装所需依赖：
   ```bash
    pip install -r requirements.txt
   ```
3. 运行脚本：
   ```bash
   python totalcode.py
   ```
4. 在提示时输入文件路径：
   ```bash
   请输入文件路径: "C:/path/to/your/file.txt"
   ```
5.  脚本将检查文件中的链接并输出结果。

## 当前状况：
我现在的状况是初步满足 nbu-icicles 项目的需求，后续将拓展文件类型和完善出自动遍历文件夹等功能。