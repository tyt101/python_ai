# 少样本
"""
提供少量典型示例（3-5 个最佳），让模型通过示例学习任务规则，
适配稍复杂的任务（如细粒度分类、格式化输出），示例需覆盖核心场景。
"""
import os
from openai import OpenAI
# ------------------- Zero Shot 核心 Prompt -------------------

"""
prompt = '''
### 任务描述

### 示例参考

### 输出要求

### 待处理内容
{input_text}
'''.strip()
"""


# 初始化客户端
client = OpenAI(
    api_key=os.getenv('DASHSCOPE_API_KEY'),
    base_url="https://dashscope.aliyuncs.com/api/v2/apps/protocols/compatible-mode/v1",
)

def call_llm(prompt):
    response = client.responses.create(
        model="qwen3-max-2026-01-23",
        input=prompt
    )
    return response.output_text

def few_shot_prompt(input_text):
    prompt = '''
    ### 任务描述
        请判断用户输入的文本的情感倾向，完成情感分类任务，参考以下示例的判断规则。
    ### 示例参考
        示例1: 文本-“抽奖抽到了周杰伦的演唱会门票，运气真好啊！”-》结果-正面
        示例2: 文本-“餐厅的菜又贵又菜又难吃，服务还很差”-〉结果-负面
        示例3: 文本-“周五了，愉快的周末来了”-》结果-正面
        示例4: 文本-“今天周三，气温25度”-〉结果-中性
    ### 输出要求
        1. 结果格式，单一标签，仅可选：正面/负面/中性
        2. 严格按示例格式输出，不得添加任何额外文字，解释或标点
        3. 无法明确判断时，统一输出“中性”
    ### 待处理内容
    {input_text}
    '''.strip()
    result_prompt = prompt.format(input_text=input_text)
    return call_llm(result_prompt)


print('结果：', few_shot_prompt('我爱假期吗？'))