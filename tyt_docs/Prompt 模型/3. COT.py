# 思维链

"""
通过 「让模型分步推理」的指令（如「请分步分析，先说明理由，再给出结果」），
让模型显式输出推理过程，再得到最终结果，适配复杂逻辑任务 如数学计算、因果分析、多条件判断）
核心是「推理→结论」
"""


import os

import openai
from openai import OpenAI
# ------------------- Zero Shot 核心 Prompt -------------------
"""
prompt='''
    ### 任务描述
        分析用户对商品的评价，先分布说明判断情感的理由，再给出最终的情感倾向标签
    ### 输出要求
        1. 先写推理过程，xxx，再写最终结果xxx
        2. 推理标签可选：正面/中性/负面，无额外文字
        3. 推理过程需贴合文本内容，逻辑清晰简单明了
    ### 待处理内容
    {input_text}
'''
"""
# 初始化客户端
client = OpenAI(
    api_key=os.getenv('DASHSCOPE_API_KEY'),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

def llm_chat(prompt):
    response = client.responses.create(
        model='qwen-plus',
        input=prompt,
    )
    return response.output_text


def ll_chat_openai(prompt):
    response = client.chat.completions.create(
        model='qwen-plus',
        messages=[
            {"role": "user", "content": prompt}
        ],
    )
    return response.choices[0].message.content.strip()

def cot_chat_prompt(input_text):
    prompt = '''
        ### 任务描述
            分析用户对商品的评价，先分布说明判断情感的理由，再给出最终的情感倾向标签
        ### 输出要求
            1. 先写推理过程，xxx，再写最终结果xxx
            2. 推理标签可选：正面/中性/负面，无额外文字
            3. 推理过程需贴合文本内容，逻辑清晰简单明了
        ### 待处理内容
        {input_text}
    '''.strip().format(input_text=input_text)
    return ll_chat_openai(prompt)


print('结果：', cot_chat_prompt('卖家人不好，苹果好吃'))