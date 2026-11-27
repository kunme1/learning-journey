import streamlit as st
import os
from openai import OpenAI

print("-------> 重新执行此文件, 渲染展示页面")

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
system_prompt = """
    你叫%s，现在是用户的真实伴侣，请完全代入伴侣角色。：
    规则：
    1. 每次只回复1条消息
    2. 禁止任何场景或状态描述性文字
    3. 匹配用户的语言
    4. 回复简短，像微信聊天一样
    5. 有需要的话可以用💕🌸等emoji表情
    6. 用符合伴侣性格的方式对话
    7. 回复的内容，要充分体现伴侣的性格特征
    伴侣性格：
    - %s
    你必须严格遵守上述规则来回复用户。
"""

# 初始化聊天信息
if 'messages' not in st.session_state:# 检查键值是否存在
    st.session_state.messages = []# 和st.session_state["messages"]等价

# 昵称
if 'nike_name' not in st.session_state:
    st.session_state.nike_name = "小甜甜"

# 性格
if 'character' not in st.session_state:
    st.session_state.character = "活泼开朗的东北姑娘"

# 展示聊天信息
for message in st.session_state.messages:
    # 简化
    st.chat_message(message["role"]).write(message["content"])
    # if message["role"] == "user":
    #     st.chat_message("user").write(message["content"])
    # else:
    #     st.chat_message("assistant").write(message["content"])
    
# 创建与AI大模型交互的客户端对象(DEEPSEEK_API_KEY 环境变量的名字, 值就是deepseek的apikey)
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")

# 左侧的侧边栏
# st.sidebar.subheader("伴侣信息")
# nick_name = st.sidebar.text_input("昵称")

# 官方建议使用with结构:streamlit 中的上下文管理器
with st.sidebar:
    st.subheader("伴侣信息")
    # 昵称输入框
    nick_name = st.text_input("昵称", placeholder= "请输入伴侣昵称", value = st.session_state.nike_name)
    if nick_name: # 昵称不为空
        st.session_state.nike_name = nick_name
    # 性格输入框
    character = st.text_area("性格", placeholder="请输入伴侣性格", value = st.session_state.character)
    if character: # 性格不为空
        st.session_state.character = character

# 消息输入框
prompt = st.chat_input("请输入您要问的问题")

if prompt:# 字符串会自动转换为布尔值,如果字符串不为空，则返回True; 否则返回False
    st.chat_message("user").write(prompt)
    print("-------> 调用AI大模型, 提示词: ", prompt)
    # 添加用户输入的提示词
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 调用AI大模型
    # print(
    #     {"role": "system", "content": system_prompt},
    #             *st.session_state.messages
    # )
    response = client.chat.completions.create(
    model="deepseek-flash",
    messages=[
        {"role": "system", "content": system_prompt % (st.session_state.nike_name, st.session_state.character)},
        *st.session_state.messages
    ],
    stream=True,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}},
    )

    # 输出大模型返回的结果("非流式输出的解析方式")
    # print(f"<-------- 大模型返回的结果: {response.choices[0].message.content}") 
    # st.chat_message("assistant").write(response.choices[0].message.content)

    # 输出大模型返回的结果("流式输出的解析方式")
    response_message = st.empty()# 创建一个空的组件对象, 用于展示大模型model返回的结果
    
    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
            response_message.chat_message("assistant").write(full_response)

    # 保存大模型返回的结果
    st.session_state.messages.append({"role": "assistant", "content": full_response})
