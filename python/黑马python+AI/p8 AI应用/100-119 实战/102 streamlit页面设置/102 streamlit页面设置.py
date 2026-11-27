import streamlit as st

# 设置页面的配置项
st.set_page_config(
    page_title="streamlit 入门",
    page_icon="🧊",
    # 布局
    layout="wide",
    # 控制的是侧边栏的状态
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.baidu.com',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# 这是一个Streamlit 的入门页面 ~"
    }
)

# 大标题
st.title("Streamlit 入门演示")
st.header("Streamlit 一级标题" )
st.subheader("Streamlit 二级标题")

# 段落文字
st.write("布偶猫是一种颜值极高、性格温顺的猫咪，因其优雅的外表和软萌的性格，被人们亲切地称为“猫界小仙女”。它拥有一双如蓝宝石般清澈明亮的眼睛，仿佛藏着一片深邃而宁静的海洋。它的毛发柔软浓密，摸起来像丝绸一样顺滑，蓬松的大尾巴宛如一把精致的羽毛扇。圆润的脸庞、粉嫩的鼻尖和灵动的耳朵，让它显得格外惹人喜爱。")
st.write("布偶猫不仅外表迷人，性格也十分讨喜。它温柔乖巧，喜欢亲近人类，常常像个小跟班一样跟在主人身后。当主人坐在沙发上休息时，它便会轻轻跳到主人的身旁，蜷缩成一个柔软的毛团，发出满足的呼噜声。阳光洒在它洁白柔软的毛发上，仿佛为它披上了一层金色的薄纱。无论是慵懒地趴在窗边，还是俏皮地追逐玩具，它都散发着独特的魅力。布偶猫就像一个降落在人间的小天使，用温柔与陪伴，为平凡的生活增添无限的温暖与快乐。")
# 图片
st.image("./earth.jpg")

# 音频
st.audio("./t-rex-roar.mp3")

# 视频
st.video("./flower.mp4")

# logo
st.logo("earth-transparent.png")


# 表格
student_data = {
    "姓名": ["王林", "李慕婉", "贝罗", "莫厉海", "石萧"],
    "学号": ["20260001", "20260002", "20260003", "20260004", "20260005"],
    "语文": [98, 90, 59, 29, 80],
    "数学": [88, 78, 65, 70, 39],
    "英语": [99, 89, 87, 59, 62],
    "总分": [285, 257, 211, 158, 181]
}
st.table(student_data)

# 输入框
name = st.text_input("请输入姓名")
st.write("您输入的姓名为:", name)

# 密码输入框
password = st.text_input("请输入密码:", type="password")
st.write("您输入的密码为:", password)

# 单选按钮
gender = st.radio("请输入您的性别", ["男", "女", "未知"], index=2)
st.write(f"您的性别为:{gender}")