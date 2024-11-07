# 这是一个示例 Python 脚本。

# 按 ⌃R 执行或将其替换为您的代码。
# 按 双击 ⇧ 在所有地方搜索类、文件、工具窗口、操作和设置。

import os

# from dotenv import load_dotenv
from openai import OpenAI

# load_dotenv('.env')

try:
    # if api_key is None:
    api_key = os.environ.get("DASHSCOPE_API_KEY")
    print(api_key)
    api_key = os.getenv("DASHSCOPE_API_KEY")
    print(api_key)
    client = OpenAI(
        # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        # 如何获取API Key：https://help.aliyun.com/zh/model-studio/developer-reference/get-api-key
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )

    completion = client.chat.completions.create(
        model="qwen-plus",  # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
        messages=[
            # {'role': 'system', 'content': 'You are a helpful assistant.'},
            # {'role': 'user', 'content': '滕王阁序全文'},
            {'role': 'user', 'content': 'python 执行URL地址，加上header与post 请求参数'},
            # {'role': 'assistant', 'content': '滕王阁序全文'},
            # {'role': 'tool', 'content': '滕王阁序全文'}
        ],

        # stream=True,#流式输出
        # stream_options={"include_usage": True}
    )
    # print(type(completion))
    # print(completion.__next__())
    # print(completion[0].choices[0].delta.content)
    print(completion)
    print(completion.choices[0].message.content)
    # # # print(completion.model_dump_json())
    # print(completion.choices[0].message)
    # for chunk in completion:
    #     print(chunk.model_dump_json())
    print(completion.model_dump_json())
except Exception as e:
    print(f"错误信息：{e}")
    print("请参考文档：https://help.aliyun.com/zh/model-studio/developer-reference/error-code")

try:
    # if api_key is None:
    api_key = os.environ.get("DASHSCOPE_API_KEY")
    print(api_key)
    api_key = os.getenv("DASHSCOPE_API_KEY")
    print(api_key)
    client = OpenAI(
        # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )
    completion = client.chat.completions.create(
        model="qwen-vl-plus",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "这是什么"},
                    {
                        "type": "image_url",
                        "image_url": {"url": "https://dashscope.oss-cn-beijing.aliyuncs.com/images/dog_and_girl.jpeg"}
                    }
                ]
            }
        ]
    )
    print(completion.model_dump_json())
except Exception as e:
    print(f"错误信息：{e}")
    print("请参考文档：https://help.aliyun.com/zh/model-studio/developer-reference/error-code")
    print("请参考文档：https://dashscope.aliyuncs.com/api/v1/tasks/ef2efdf6-823c-4ad4-975b-1a4253e2e612")
