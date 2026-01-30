# 自我一致性
"""
CoT 的升级版本，
核心是「多次生成推理过程→从多个结果中投票选出最一致的答案」，解决复杂任务中模型推理结果不稳定的问题，步骤为：
多次调用 CoT 模型，得到多个「推理过程 + 结果」；
提取所有结果，统计出现次数；
票数最高的结果为最终答案（一致性最高）。
"""

import os
from openai import OpenAI


client = OpenAI(
    api_key=os.getenv('DASHSCOPE_API_KEY'),
    base_url="https://dashscope.aliyuncs.com/api/v2/apps/protocols/compatible-mode/v1",
)


def llm_chat(prompt):
    client.responses.create(
        model='',
        input=prompt,
    )

