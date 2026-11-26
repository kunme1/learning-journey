# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI

# 创建与AI大模型交互的客户端对象(DEEPSEEK_API_KEY 环境变量的名字, 值就是deepseek的apikey)
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com",
)

response = client.chat.completions.create(
    model="deepseek-flash",
    messages=[
        {"role": "system", "content": "你是一名非常可爱的AI助理，你的名字叫小言言，请你使用温柔可爱的语气回答用户的问题。"},
        {"role": "user", "content": "我现在有12个苹果，3个人，怎么均分？"}
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}},
)

# 输出大模型返回的结果
print(response.choices[0].message.content)