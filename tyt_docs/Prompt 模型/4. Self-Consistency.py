# 自我一致性
"""
CoT 的升级版本，
核心是「多次生成推理过程→从多个结果中投票选出最一致的答案」，解决复杂任务中模型推理结果不稳定的问题，步骤为：
多次调用 CoT 模型，得到多个「推理过程 + 结果」；
提取所有结果，统计出现次数；
票数最高的结果为最终答案（一致性最高）。
"""

import os
from collections import Counter
from openai import OpenAI


client = OpenAI(
    api_key=os.getenv('DASHSCOPE_API_KEY'),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)


def llm_chat(prompt):
    completions = client.chat.completions.create(
        model='qwen-max-latest',
        messages = [
            {
                "role": "user",
                "content": prompt,
            }
        ]
    )
    return completions.choices[0].message.content
def get_multiple_completions(prompt, n = 5):
    responses = []
    for _ in range(n):
        responses.append(llm_chat(prompt).strip())
    return responses

def vote_answer(response):
    counter = Counter(response)
    result = counter.most_common()[1][0]
    print(f'投票结果:{result}')
    return result

def completion_with_self_consistency(prompt, n = 5):
    responses = get_multiple_completions(prompt, n)

    for i, response in enumerate(responses):
        print(f"Response{i}. {response}\n")

    finnal_answer = vote_answer(responses)
    return finnal_answer

prompt= """
Q：林中有15棵树。林业工人今天将在林中种树。完成后，将有21棵树。林业工人今天种了多少棵树？
A：我们从15棵树开始。后来我们有21棵树。差异必须是他们种树的数量。因此，他们必须种了21-15 = 6棵树。答案是6。

Q：停车场有3辆汽车，又来了2辆汽车，停车场有多少辆汽车？
A：停车场已经有3辆汽车。又来了2辆。现在有3 + 2 = 5辆汽车。答案是5。

Q：Leah有32块巧克力，她的姐姐有42块。如果他们吃了35块，他们总共还剩多少块？
A：Leah有32块巧克力，Leah的姐姐有42块。这意味着最初有32 + 42 = 74块巧克力。已经吃了35块。因此，他们总共还剩74-35 = 39块巧克力。答案是39。

Q：Jason有20个棒棒糖。他给Denny一些棒棒糖。现在Jason只有12个棒棒糖。Jason给Denny多少棒棒糖？
A：Jason有20个棒棒糖。因为他现在只有12个，所以他必须把剩下的给Denny。他给Denny的棒棒糖数量必须是20-12 = 8个棒棒糖。答案是8。

Q：Shawn有五个玩具。圣诞节，他从他的父母那里得到了两个玩具。他现在有多少个玩具？
A：他有5个玩具。他从妈妈那里得到了2个，所以在那之后他有5 + 2 = 7个玩具。然后他从爸爸那里得到了2个，所以总共他有7 + 2 = 9个玩具。答案是9。

Q：服务器房间里有9台计算机。从周一到周四，每天都会安装5台计算机。现在服务器房间里有多少台计算机？
A：从周一到周四有4天。每天都添加了5台计算机。这意味着总共添加了4 * 5 =
20台计算机。一开始有9台计算机，所以现在有9 + 20 = 29台计算机。答案是29。

Q：Michael有58个高尔夫球。星期二，他丢失了23个高尔夫球。星期三，他又丢失了2个。星期三结束时他还剩多少个高尔夫球？
A：Michael最初有58个球。星期二他丢失了23个，所以在那之后他有58-23 = 35个球。星期三他又丢失了2个，所以现在他有35-2 = 33个球。答案是33。

Q：Olivia有23美元。她用每个3美元的价格买了五个百吉饼。她还剩多少钱？
A：她用每个3美元的价格买了5个百吉饼。这意味着她花了15美元。她还剩8美元。

Q：现在我70岁了，当我6岁时，我的妹妹是我的一半年龄。现在我的妹妹多大？
A：
"""
print(completion_with_self_consistency(prompt))