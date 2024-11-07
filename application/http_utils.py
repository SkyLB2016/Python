# -*- coding: utf-8 -*-
"""
@Time    : 2024/11/7 11:31
@Author  : sky
@Email   : your-email@example.com
@File    : down_file.py
@Description: 
"""


# b360b3e4-3cbe-4d72-8e42-de2c618bc1f9
# e0648b4d-d103-4b9c-81e8-01dd8f9f42e0
import urllib.request
import urllib.parse
import requests

import urllib.request

url = 'https://dashscope.aliyuncs.com/api/v1/services/aigc/text2image/image-synthesis'
# 发送 GET 请求
response = urllib.request.urlopen(url)
# 读取响应内容
content = response.read().decode('utf-8')
print('响应内容:', content)


url = 'https://dashscope.aliyuncs.com/api/v1/services/aigc/text2image/image-synthesis'
# 定义请求数据
data = {
    'key1': 'value1',
    'key2': 'value2'
}
# 将数据编码为字节串
data = urllib.parse.urlencode(data).encode('utf-8')
# 发送 POST 请求
response = urllib.request.urlopen(url, data=data)
# 读取响应内容
content = response.read().decode('utf-8')
print('响应内容:', content)


### 使用 `requests` 库
# `requests` 是一个非常流行的HTTP库，使用起来非常简单。首先，你需要安装它：
# 然后，你可以使用以下代码来执行URL地址并获取其内容：
url = 'https://dashscope.aliyuncs.com/api/v1/services/aigc/text2image/image-synthesis'
response = requests.get(url)
# 检查请求是否成功
if response.status_code == 200:
    print('请求成功')
    print('响应内容:', response.text)
else:
    print('请求失败，状态码:', response.status_code)

### 使用 `urllib` 库
# `urllib` 是Python标准库的一部分，不需要额外安装。以下是一个使用 `urllib` 的示例：
url = 'https://dashscope.aliyuncs.com/api/v1/services/aigc/text2image/image-synthesis'
try:
    with urllib.request.urlopen(url) as response:
        content = response.read().decode('utf-8')
        print('请求成功')
        print('响应内容:', content)
except urllib.error.URLError as e:
    print('请求失败，错误:', e)

### 解析HTML内容
# 如果你需要解析从URL获取的HTML内容，可以使用 `BeautifulSoup` 库。首先，安装 `beautifulsoup4`：
# 然后，结合 `requests` 或 `urllib` 来解析HTML内容：
#### 使用 `requests` 和 `BeautifulSoup`
import requests
from bs4 import BeautifulSoup
url = 'https://dashscope.aliyuncs.com/api/v1/services/aigc/text2image/image-synthesis'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    print('请求成功')
    print('标题:', soup.title.string)
else:
    print('请求失败，状态码:', response.status_code)

#### 使用 `urllib` 和 `BeautifulSoup`
import urllib.request
from bs4 import BeautifulSoup

url = 'https://dashscope.aliyuncs.com/api/v1/services/aigc/text2image/image-synthesis'

try:
    with urllib.request.urlopen(url) as response:
        content = response.read().decode('utf-8')
        soup = BeautifulSoup(content, 'html.parser')
        print('请求成功')
        print('标题:', soup.title.string)
except urllib.error.URLError as e:
    print('请求失败，错误:', e)




# 在 Python 中，你可以使用 `requests` 库来发送 HTTP 请求。以下是一个示例代码，展示了如何发送带有自定义头部（headers）和 POST 请求参数的请求。
# 首先，确保你已经安装了 `requests` 库。如果没有安装，可以使用以下命令进行安装：
# 然后，你可以使用以下代码来执行带有头部和 POST 请求参数的 URL 请求：

# 定义URL
url = 'https://dashscope.aliyuncs.com/api/v1/services/aigc/text2image/image-synthesis'

# 定义请求头
headers = {
    'X-DashScope-Async': 'enable',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer sk-57134a934d3d4d2d99d84d2812f88424'
}

# 定义POST请求参数
data = {
        "model": "wanx-v1",
        "input": {
            "prompt": "日本美少女，长腿裸体内衣，高分辨率，增加细节，细节强化，正面视角，肤若凝脂，面如冠玉，精致的脸部比例，极高分辨率，清晰度强化，高光"
        },
        "parameters": {
            "style": "<auto>",
            "size": "720*1280",
            "n":1
        }
    }

# 发送POST请求
response = requests.post(url, headers=headers, json=data)

# 检查响应状态码
if response.status_code == 200:
    print('请求成功')
    # 打印响应内容
    print(response.json())
    content = response.json()
    print(content['output']['task_id'])
else:
    print(f'请求失败，状态码: {response.status_code}')
    # 打印响应内容
    print(response.text)
### 解释
# 1. **导入 `requests` 库**：首先导入 `requests` 库。
# 2. **定义 URL**：设置你要请求的 URL。
# 3. **定义请求头**：创建一个字典来存储请求头信息。常见的头部包括 `Content-Type` 和 `Authorization`。
# 4. **定义 POST 请求参数**：创建一个字典来存储 POST 请求的数据。这里使用 `json` 参数将数据转换为 JSON 格式。
# 5. **发送 POST 请求**：使用 `requests.post` 方法发送 POST 请求，并传递 URL、头部和数据。
# 6. **检查响应状态码**：检查响应的状态码，如果是 200 表示请求成功。
# 7. **处理响应**：根据响应状态码处理响应内容。如果请求成功，打印响应的 JSON 内容；如果请求失败，打印错误信息和响应内容。