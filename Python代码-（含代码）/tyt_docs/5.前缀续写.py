import os
from openai import OpenAI

# 1. 初始化客户端
client = OpenAI(
    # 若没有配置环境变量，请将下行替换为：api_key="sk-xxx"
    # 各地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    # 以下是北京地域base-url，如果使用新加坡地域的模型，需要将base_url替换为：https://dashscope-intl.aliyuncs.com/compatible-mode/v1
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

# 2. 定义需要补全的代码前缀
prefix = """def calculate_fibonacci(n):
    if n <= 1:
        return n
    else:
"""

# 3. 发起 Partial Mode 请求
# 注意：messages 数组的最后一条消息 role 为 "assistant"，并包含 "partial": True
completion = client.chat.completions.create(
    model="qwen3-coder-plus",
    messages=[
        {"role": "user", "content": "请补全这个斐波那契函数，勿添加其它内容"},
        {"role": "assistant", "content": prefix, "partial": True},
    ],
)

# 4. 手动拼接前缀和模型生成的内容
generated_code = completion.choices[0].message.content
complete_code = prefix + generated_code

print(complete_code)