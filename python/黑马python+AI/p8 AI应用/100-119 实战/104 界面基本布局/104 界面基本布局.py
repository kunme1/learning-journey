import streamlit as st
import os
from openai import OpenAI

# 设置页面的配置项
st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🤖",
    # 布局
    layout="wide",
    # 控制的是侧边栏的状态
    initial_sidebar_state="expanded",
    menu_items={}
)

# 大标题
st.title("AI智能伴侣")

# logo
st.logo("./logo.png")

# 系统提示词
system_prompt = "你是一名非常可爱的AI助理，你的名字叫小言言，请你使用温柔可爱的语气回答用户的问题。"


# 创建与AI大模型交互的客户端对象(DEEPSEEK_API_KEY 环境变量的名字, 值就是deepseek的apikey)
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")

# 消息输入框
prompt = st.chat_input("请输入您要问的问题")
if prompt:# 字符串会自动转换为布尔值,如果字符串不为空，则返回True; 否则返回False
    st.chat_message("user").write(prompt)
    print("-------> 调用AI大模型, 提示词: ", prompt)

    # 调用AI大模型
    response = client.chat.completions.create(
    model="deepseek-flash",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt}
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}},
    )

    # 输出大模型返回的结果
    print(f"<-------- 大模型返回的结果: {response.choices[0].message.content}") 
    st.chat_message("assistant").write(response.choices[0].message.content)