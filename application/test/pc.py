# import urllib.request
# # 请求的URL
# url = "http://httpbin.org/get"
# # 模拟浏览器打开网页(get请求)
# res = urllib.request.urlopen(url)
# print(res.read().decode("utf-8"))
import os
# import urllib.request
# import urllib.parse
#
# url = "http://httpbin.org/post"
# # 按POST请求的格式封装数据，请求内容，需要传递data
# data = bytes(urllib.parse.urlencode({"hello": "world"}), encoding="utf-8")
# res = urllib.request.urlopen(url, data=data)
# # 输出响应结果
# print(res.read().decode("utf-8"))

# import urllib.request
#
# url = "http://douban.com"
# resp = urllib.request.urlopen(url)
# print(resp.read().decode('utf-8'))
# # 返回错误：反爬虫
# # raise HTTPError(req.full_url, code, msg, hdrs, fp)
# # urllib.error.HTTPError: HTTP Error 418:
# #
# # HTTP 418 I'm a teapot客户端错误响应代码表示服务器拒绝煮咖啡，因为它是一个茶壶。这个错误是对1998年愚人节玩笑的超文本咖啡壶控制协议的引用。


import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# url = "http://douban.com"
# # 自定义headers
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
# }
# req = urllib.request.Request(url, headers=headers)
# # urlopen(也可以是request对象)
# print(urllib.request.urlopen(req).read().decode('utf-8'))  # 获取字符串内容，需要指定解码方式

# 超时设置
# import urllib.request,urllib.error
#
# url = "http://httpbin.org/get"
# try:
#     resp = urllib.request.urlopen(url, timeout=0.01)
#     print(resp.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     print("time out")
#

# 将远程的数据保存成文件
# urlretrieve(url, filename=None, reporthook=None, data=None)
# # 参数说明
# url：传入的网址
# filename：指定了保存本地路径（如果参数未指定，urllib会生成一个临时文件保存数据)
# reporthook：是一个回调函数，当连接上服务器、以及相应的数据块传输完毕时会触发该回调，我们可以利用这个回调函数来显示当前的下载进度
# data：指 post 到服务器的数据，该方法返回一个包含两个元素的(filename, headers)元组，filename 表示保存到本地的路径，header表示服务器的响应头


import urllib.request

# url = "http://www.hao6v.com/"
# filename = '../static/video.html'


# def callback(blocknum, blocksize, totalsize):
#     """
#         @blocknum:目前为此传递的数据块数量
#         @blocksize:每个数据块的大小，单位是byte,字节
#         @totalsize:远程文件的大小
#     """
#     if totalsize == 0:
#         percent = 0
#     else:
#         percent = blocknum * blocksize / totalsize
#     if percent > 1.0:
#         percent = 1.0
#     percent = percent * 100
#     print("download : %.2f%%" % (percent))
#
#
# local_filename, headers = urllib.request.urlretrieve(url, filename, callback)


# urllib.error 模块为 urllib.request 所引发的异常定义了异常类，基础异常类是 URLError。
# 所有HTTP响应的第一行都是状态行，依次是当前HTTP版本号，3位数字组成的状态代码，以及描述状态的短语，彼此由空格分隔。
#
# 状态代码的第一个数字代表当前响应的类型：
#
# 1xx消息——请求已被服务器接收，继续处理
# 2xx成功——请求已成功被服务器接收、理解、并接受
# 3xx重定向——需要后续操作才能完成这一请求
# 4xx请求错误——4xx类的状态码用于看起来客户端有错误的情况下，请求含有词法错误或者无法被执行
# 5xx服务器错误——由数字“5”打头的响应状态码表示服务器已经明显处于错误的状况下或没有能力执行请求，或在处理某个正确请求时发生错误。

# import urllib.request,urllib.error
#
# try:
#     url = "http://www.baidus.com"
#     resp = urllib.request.urlopen(url)
#     print(resp.read().decode('utf-8'))
# # except urllib.error.HTTPError as e:
# #     print("请检查url是否正确")
# # URLError是urllib.request异常的超类
# except urllib.error.URLError as e:
#     if hasattr(e, "code"):
#         print(e.code)
#     if hasattr(e, "reason"):
#         print(e.reason)
