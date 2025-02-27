# AutoCheck_BaiduNetdiskLinks
Auto check links in texts to make sure they are available.  
Originally used for the nbu-icicles project.

## Overview:
- A preliminary script initially developed for the nbu-icicles project, used to verify whether links in files (webpages) have expired.
- The current development goal is to implement automatic checking of Baidu Netdisk links.
- In the future, it will support OneDrive, Quark, Xunlei, and other cloud storage services.

## Requirements:
- Selenium 4.24.0 (or similar)

## Current Status:
I am currently facing the problem that I have no way to automatically retrieve the content from Baidu Netdisk links. At the moment, the only solution I can think of is to use Selenium for web automation, but it seems that Selenium requires installing plugins, and the official Baidu Netdisk API appears to be accessible only to enterprise users. That’s it for today; I'll continue writing when I have more ideas.


---
#### 中文版
# AutoCheck_BaiduNetdiskLinks
## 简述：
- 一个初步为nbu-icicles项目开发的脚本，用于确认文件（网页）中的链接是否过期。
- 当前开发目标为实现自动检查百度网盘链接
- 将来会支持onedrive、夸克、迅雷等网盘

## 需求：
- Selenium 4.24.0（或类似版本？）

## 当前状况：
我现在遇到的问题是，我没有办法自动获取百度网盘链接中的内容。目前，唯一的解决思路是使用 Selenium 实现网页自动化，但似乎 Selenium 需要安装插件，而百度网盘的官方 API 接口又仅对企业用户开放。今天先到这里，想到再继续写。