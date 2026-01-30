import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)
messages = [
    {
        "role": "user",
        "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20251031/ownrof/f26d201b1e3f4e62ab4a1fc82dd5c9bb.png"
                    },
                },
            {"type": "text", "text": "请问图片展现了有哪些商品？"},
        ],
    }
]
completion = client.chat.completions.create(
    model="qwen3-vl-plus",
    messages=messages,
)
print(completion.choices[0].message.content)
print(completion.choices[0].message.content)