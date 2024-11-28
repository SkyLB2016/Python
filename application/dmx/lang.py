# -*- coding: utf-8 -*-
"""
@Time    : 2024/11/13 19:04
@Author  : sky
@Email   : your-email@example.com
@File    : lang.py
@Description: 
"""


import langchain
import requests

# 假设的API URL
API_URL = "https://api.example.com/data"


# 发送HTTP GET请求到API并获取数据
def get_data_from_api(query):
    response = requests.get(f"{API_URL}?query={query}")
    if response.status_code == 200:
        return response.json()
    else:
        return None


# 创建PromptTemplater并定义模板
prompt_templater = langchain.PromptTemplater(
    template="Here is the data for your query: {{ get_data_from_api(query='QUERY') }}"
)

# 使用PromptTemplater生成提示
query = "weather in New York"
prompt = prompt_templater.format(locals())

# 假设的get_data_from_api函数应该返回天气数据的字典
# 这里我们直接模拟调用API并获取结果
api_response = {
    "temperature": "72°F",
    "weather": "Sunny",
    "wind": "10 mph"
}

# 将模拟的API响应存储在一个局部变量中
context = {"get_data_from_api": lambda query: api_response}

# 使用模型生成响应
response = model.generate_text(prompt, context=context)
print(response)