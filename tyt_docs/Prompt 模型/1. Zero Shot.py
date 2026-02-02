# 0 样本

"""
Zero-Shot（零样本）提示词的核心是不提供任何示例，
仅通过清晰的任务描述、输出要求、格式规范让模型理解并完成任务，
关键要做到「任务明确、约束清晰、格式统一」
"""
import os
from openai import OpenAI

# ------------------- Zero Shot 核心 Prompt -------------------
"""
prompt = '''
### 任务描述
请你判断用户输入文本的情感倾向，完成情感分类任务。
### 输出要求
1. 结果格式：单一标签，仅可选：正面/负面/中性；
2. 严格按选项输出，不得添加任何额外文字、解释或标点；
3. 无法明确判断情感时，统一输出"中性"。
### 待处理内容
{input_text}
'''.strip()
"""
# -------------------------------------------------------------

# 初始化客户端
client = OpenAI(
    api_key=os.getenv('DASHSCOPE_API_KEY'),
    base_url="https://dashscope.aliyuncs.com/api/v2/apps/protocols/compatible-mode/v1",
)
# ------------------------------封装一下-------------------------------

def call_llm(prompt):
    response = client.responses.create(
        model="qwen3-max-2026-01-23",
        input=prompt
    )
    return response.output_text

def zero_shot_prompt(input_text):
    prompt = '''
    ### 任务描述
    请你判断用户输入文本的情感倾向，完成情感分类任务。
    ### 输出要求
    1. 结果格式：单一标签，仅可选：正面/负面/中性；
    2. 严格按选项输出，不得添加任何额外文字、解释或标点；
    3. 无法明确判断情感时，统一输出"中性"。
    ### 待处理内容
    {input_text}
    '''.strip().format(input_text=input_text)

    call_llm(prompt)