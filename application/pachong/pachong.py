#导入内置模块
import sys
#导入标准库
import os
#导入第三方库（需要安装：pip install bs4）
# import bs4
# from bs4 import BeautifulSoup

# print(os.getcwd()) #打印当前工作目录
# #import bs4 导入整个模块
# print(bs4.BeautifulSoup.getText)
# #from bs4 import BeautifulSoup 导入指定模块的部分属性至当前工作空间
# print(BeautifulSoup.getText)

import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
# url = "https://www.baidu.com/"
# url = "https://www.baidu.com/index.php?tn=monline_3_dg"
url = "https://mp.weixin.qq.com/s/A4k3fSQEjTxgKhuq5E0fYw"
res = urllib.request.urlopen(url)  # get方式请求
# print("res",res)  # 返回HTTPResponse对象<http.client.HTTPResponse object at 0x00000000026D3D00>
# 读取响应体
bys = res.read()  # 调用read()方法得到的是bytes对象。
# print("bys",bys)  # <!DOCTYPE html><!--STATUS OK-->\n\n\n    <html><head><meta...

# 转成对应的文本内容
content = bys.decode("utf-8")
print("bys.decode(utf-8)",content)  # 获取字符串内容，需要指定解码方式,这部分我们放到html文件中就是百度的主页
#
# # 获取HTTP协议版本号(10 是 HTTP/1.0, 11 是 HTTP/1.1)
# print("res.version",res.version)  # 11
#
# # 获取响应码 以及 响应描述字符串
# print("res.getcode",res.getcode())  # 200
# print("res.status",res.status)  # 200
# print("res.reason",res.reason)  # OK
#
# # 获取实际请求的页面url(防止重定向用)
# # print("res.geturl",res.geturl())  # http://www.baidu.com/
#
# # 获取响应头信息,返回字符串
# print("res.info",res.info())  # Bdpagetype: 1 Bdqid: 0x803fb2b9000fdebb...
# # 获取响应头信息,返回二元元组列表
# print("res.getheaders",res.getheaders())  # [('Bdpagetype', '1'), ('Bdqid', '0x803fb2b9000fdebb'),...]
# print("res.getheaders",res.getheaders()[0])  # ('Bdpagetype', '1')
# # 获取特定响应头信息
# print("res.getheader",res.getheader(name="Content-Type"))  # text/html;charset=utf-8

