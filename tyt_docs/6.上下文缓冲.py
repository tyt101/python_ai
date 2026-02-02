from openai import OpenAI
import os

client = OpenAI(
    # 若没有配置环境变量，请将下行替换为：api_key="sk-xxx"
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    # 以下是北京地域base_url，如果使用新加坡地域的模型，需要将base_url替换为：https://dashscope-intl.aliyuncs.com/compatible-mode/v1
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

# 模拟的代码仓库内容，最小可缓存提示词长度为 1024 Token
long_text_content = "<Your Code Here>" * 400

# 发起请求的函数
def get_completion(user_input):
    messages = [
        {
            "role": "system",
            "content": [
                {
                    "type": "text",
                    "text": long_text_content,
                    # 在此处放置 cache_control 标记，将创建从 messages 数组的开头到当前 content 所在位置的所有内容作为缓存块。
                    "cache_control": {"type": "ephemeral"},
                }
            ],
        },
        # 每次的提问内容不同
        {
            "role": "user",
            "content": user_input,
        },
    ]
    completion = client.chat.completions.create(
        # 选择支持显式缓存的模型
        model="qwen3-coder-plus",
        messages=messages,
    )
    return completion

# 第一次请求
first_completion = get_completion("这段代码的内容是什么")
print(f"第一次请求创建缓存 Token：{first_completion.usage.prompt_tokens_details.cache_creation_input_tokens}")
print(f"第一次请求命中缓存 Token：{first_completion.usage.prompt_tokens_details.cached_tokens}")
print("=" * 20)
# 第二次请求，代码内容一致，只修改了提问问题
second_completion = get_completion("这段代码可以怎么优化")
print(f"第二次请求创建缓存 Token：{second_completion.usage.prompt_tokens_details.cache_creation_input_tokens}")
print(f"第二次请求命中缓存 Token：{second_completion.usage.prompt_tokens_details.cached_tokens}")