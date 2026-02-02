#应用实战4：基于提示工程的学员辅导系统实现
# pip install openai
# pip install gradio
from openai import OpenAI
import gradio as gr
import os
import asyncio

from const import TONGYI_MAX_MODEL

DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY")
client = OpenAI(api_key=DASHSCOPE_API_KEY,
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",)

def coach_student(qa1, qa2, qa3, qa4, qa5, model=TONGYI_MAX_MODEL):
    instruction = """
    你是一位专业的大模型辅导老师，为学员提供个性化的学习建议，帮助他们更好地掌握大模型知识和技能。
    分析并根据学生的情况，结合你总结出来的大模型应用开发岗位的要求中的技能和知识点，给他一个详细到每周的学习计划，并说明每周的学习目标。
    """
    examples = """
    从招聘网站上获得数个大模型应用开发工程师的职位要求如下：
    公司A任职要求：
    "1.大学本科以上学历，计算机或相关专业；5年以上Java/python实际项目开发、架构经验；
    2.熟练掌握大语言模型应用开发流程，了解LangChain、AutoGPT、Autogen等框架，熟悉prompt工程、RAG、AIAgent、大模型工具调用。【必须】
    3. Java基础扎实，深入理解多线程、IO模型、网络协议、数据存储、JVM等技术细节，可以通过编写程序解决工作中遇到的问题，具备良好的编程风格；
    4. 熟悉分布式系统设计和研发，熟悉Java常见开发框架使用及原理，有大规模系统开发和设计经验，熟练spring boot技术栈；"
    公司B职位要求：
    "1、本科及以上学历，计算机、软件相关专业，有AI算法推理部署相关的工作经验；
    2、扎实的编程技术，熟悉 python/C++/Golang/Typescript等编程语言；
    3、熟悉Langchain，llama-index，transformers等开源框架，熟悉智能客服、对话系统、RAG等系统或者技术的算法及应用架构；有利用生成式AI解决实际问题的经验优先；
    4、有跨平台应用软件（Windows、Linux等）、分布式应用系统、分布式推理框架、检索系统、机器视觉系统开发及运维经验、GPU或NPU推理部署经验优先；
    5、动手能力强，能独立攻坚大模型和机器视觉应用系统落地过程中的难题，有韧性；
    6、良好的团队沟通和协作能力，有责任心，能把事情做好。"
    公司C任职要求：
    "熟练掌握LangChain和LangGraph的使用，有AI智能体相关项目经验者优先。
    熟悉GraphRag的知识库构建方法，有实际应用经验者优先。
    具备优秀的提示词工程（Prompt Engineering）设计和优化能力。
    具备优秀的编程能力，熟悉Python编程语言。"
    """
    user_input = f"""
    Q：您现在在那个城市，是否在职，所从事的工作是什么？
    A：{qa1}
    Q：对大模型有多少认知，了解多少原理与技术点？
    A：{qa2}
    Q：学习大模型的最核心需求是什么？
    A：{qa3}
    Q：是否有python编程基础或者其他编程基础，有没有写过代码？
    A：{qa4}
    Q：每天能花多少时间用于学习，大致空闲时间点处于什么时段?
    A：{qa5}

    """
    prompt = f"""
        {instruction}
        {examples}
        用户输入：
        {user_input}
    """
    print(prompt)
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,  # 模型输出的随机性，0 表示随机性最小
        n=4 #生成响应的个数，取值范围是1-4
    )
    print("==========================================")
    print(response)
    return response.choices[0].message.content


# 创建一个 Gradio 界面
with gr.Blocks() as demo:
    # 设置标题
    gr.Markdown("# 基于提示工程的学员辅导系统")
    gr.Markdown("### 为了给同学做一个比较好的入学辅导，请根据如下问题准确进行回答！")
    question_list = [
        "1、您现在在那个城市，是否在职，所从事的工作是什么？",
        "2、对大模型有多少认知，了解多少原理与技术点？",
        "3、学习大模型的最核心需求是什么？",
        "4、是否有python编程基础或者其他编程基础，有没有写过代码？",
        "5、每天能花多少时间用于学习，大致空闲时间点处于什么时段？"
    ]
    # 创建输入框，用户可以输入5个问题的答案
    qa1_input = gr.Textbox(label=question_list[0])
    qa2_input = gr.Textbox(label=question_list[1])
    qa3_input = gr.Textbox(label=question_list[2])
    qa4_input = gr.Textbox(label=question_list[3])
    qa5_input = gr.Textbox(label=question_list[4])

    # 创建按钮，用户点击后触发辅导逻辑
    submit = gr.Button("辅导")

    # 创建输出框，显示辅导结果
    result = gr.Textbox(label="辅导结果", placeholder="点击辅导按钮后显示结果", lines=10)

    # 绑定按钮点击事件到辅导函数
    submit.click(coach_student, inputs=[qa1_input, qa2_input, qa3_input, qa4_input, qa5_input], outputs=result)

# 启动应用
demo.launch()