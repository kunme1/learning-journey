# Streamlit参考手册

> 原文：[飞书云文档](https://heuqqdmbyk.feishu.cn/wiki/Uf4ewHktYiYMZdk6G4icXfHXnwb)

## 1. Streamlit介绍与安装

- 官方网站：<https://streamlit.io/>
- 能在几分钟内把 `Python` 脚本变成可分享的网站。只需使用纯 `Python` ，无需前端经验。甚至，你只需要懂 `markdown` ，然后按照一定规则去做也能搞个网页出来。它还支持免费部署，感动到落泪。

[Streamlit 介绍视频（MP4）](./Streamlit参考手册-assets/hero-video.mp4)

- 安装：`pip install streamlit`

## 2. Streamlit基础用法

### 2.1 标题title

使用 `st.title()` 可以设置标题内容。

```python
import streamlit as st

st.title('Python从入门到大神')
```

效果:

![2.1 标题title效果截图](./Streamlit参考手册-assets/01.png)

### 2.2 段落write

段落就是 `HTML` 里的 `<p>` 元素，在 `streamlit` 里使用 `st.write('内容')` 的方式去书写。

```python
import streamlit as st

st.write('Hello')
```

效果:

![2.2 段落write效果截图](./Streamlit参考手册-assets/02.png)

### 2.3 使用markdown

`streamlit` 是支持使用 `markdown` 语法来写页面内容的，只需使用单引号或者双引号的方式将内容包起来，并且使用 `markdown` 的语法进行书写，页面就会出现对应样式的内容。

```python
import streamlit as st

"# 1级标题"
"## 2级标题"
"### 3级标题"
"#### 4级标题"
"##### 5级标题"
"###### 6级标题"
```

效果:

![2.3 使用markdown效果截图](./Streamlit参考手册-assets/03.png)

### 2.4 图片image

渲染图片可以使用 `st.image()` 方法，也可以使用 `markdown` 的语法。

`st.image(图片地址, [图片宽度])` ，其中图片宽度不是必填项。

```python
import streamlit as st

st.image('./cat.jpg', width=400)
```

效果:

![2.4 图片image效果截图](./Streamlit参考手册-assets/04.png)

### 2.5 表格table

静态表格使用 `st.table()` 渲染，出来的效果就是 `HTML` 的 `<table>`。

`st.table()` 支持传入字典等数据。

```python
import streamlit as st

data = {"姓名": ["王林", "李慕婉", "贝罗", "莫厉海", "石萧", "红蝶", "十三"],
        "学号": ["20230001", "20230002", "20230003", "20230004", "20230005", "20230006", "20230007"],
        "语文": [80, 90, 85, 70, 95, 90, 85],
        "数学": [87, 92, 87, 81, 92, 69, 83],
        "英语": [90, 85, 90, 95, 80, 85, 90],
        "总分": [257, 267, 262, 241, 267, 244, 258]}
st.table(data)
```

效果:

![2.5 表格table效果截图](./Streamlit参考手册-assets/05.png)

### 2.6 分割线divider

分隔线就是 `HTML` 里的 `<hr>` 。在 `streamlit` 里使用 `st.divider()` 方法绘制分隔线。

```python
import streamlit as st

st.divider()
```

效果:

![2.6 分割线divider效果截图](./Streamlit参考手册-assets/06.png)

### 2.7 输入框

知道怎么声明变量后，可以使用一个变量接收输入框的内容。

输入框又可以设置不同的类型，比如普通的文本输入框、密码输入框。

#### 2.7.1 普通输入框 text_input

输入框使用 `st.text_input()` 渲染。

```python
import streamlit as st

# 输入框
name = st.text_input("请输入你的姓名：")

if name:
    st.write("你好, ", name)
```

效果:

![2.7.1 普通输入框 text_input效果截图](./Streamlit参考手册-assets/07.png)

#### 2.7.2 密码 text_input

如果要使用密码框，可以给 `st.text_input()` 加多个类型 `type="password"`。

```python
import streamlit as st

# 密码
password = st.text_input("请输入你的密码：", type="password")

if password:
    st.write(f"你的密码是{password}吗?")
```

效果:

![2.7.2 密码 text_input效果截图](./Streamlit参考手册-assets/08.png)

#### 2.7.3 数字输入框 number_input

数字输入框需要使用 `number_input`

```python
import streamlit as st

age = st.number_input('年龄：')

st.write(f'你输入的年龄是{age}岁')
```

众所周知，正常表达年龄是不带小数位的，所以我们可以设置 `st.number_input()` 的步长为1，参数名叫 `step`。

```python
# 省略部分代码

st.number_input('年龄：', step=1)
```

这个步长可以根据你的需求来设置，设置完后，输入框右侧的加减号每点击一次就根据你设置的步长相应的增加或者减少。

还有一点，人年龄不可能是负数，通常也不会大于200。可以通过 `min_value` 和 `max_value` 设置最小值和最大值。同时还可以通过 `value` 设置默认值。

```python
st.number_input('年龄：', value=20, min_value=0, max_value=200, step=1)
```

效果:

![2.7.3 数字输入框 number_input效果截图](./Streamlit参考手册-assets/09.png)

#### 2.7.4 多行文本框 text_area

创建多行文本框使用的是 `st.text_area()`，用法和 `st.text_input()` 差不多。

```python
import streamlit as st

paragraph = st.text_area("多行内容：")
```

效果:

![2.7.4 多行文本框 text_area效果截图](./Streamlit参考手册-assets/10.png)

#### 2.7.5 复选框 checkbox

很多应用在登录之前需要用户同意某些协议才能使用，如果你网站也需要这个功能的话可以使用复选框 `st.checkbox()` 让用户去勾选。

```python
import streamlit as st

checked = st.checkbox("同意以上条款")
if checked:
  st.write("同意")
else:
  st.write("不同意")
```

效果:

![2.7.5 复选框 checkbox效果截图](./Streamlit参考手册-assets/11.png)

#### 2.7.6 单选框 radio

使用 `st.radio()` 可以制作单选按钮，比如让用户选择性别的时候就能派上用场。

```python
import streamlit as st

# 单选按钮
is_ok = st.radio("密码正确吗? ", ["正确", "错误"], index=1)

if is_ok:
    st.write(f"密码是{is_ok}的")
```

单选按钮也可以使用一个变量来接收结果。

它还支持设置默认值，使用 `index` 参数即可。`index` 的默认值是1，也就是选中下标为 1 的那项。可以根据你的需求自定义设置。

```python
import streamlit as st

# 单选按钮
is_ok = st.radio("密码正确吗? ", ["正确", "错误"], index=1)

if is_ok:
    st.write(f"密码是{is_ok}的")
```

效果:

![2.7.6 单选框 radio效果截图](./Streamlit参考手册-assets/12.png)

#### 2.7.7 单选下拉框 selectbox

使用 `st.selectbox()` 可以创建单选下拉框。

用法是：

```python
import streamlit as st

subject = st.selectbox(
  "意向学科",
  [
    "AI大模型开发",
    "AI智能应用开发",
    "AI嵌入式+机器人开发",
    "AI测试",
    "AI运维"
  ]
)

st.write(f"你喜欢{subject }")
```

效果:

![2.7.7 单选下拉框 selectbox效果截图](./Streamlit参考手册-assets/13.png)

#### 2.7.8 多选下拉框 multiselect

使用 `st.multiselect()` 可以创建多选下拉框，用法和 `st.selectbox()` 一样。

```python
import streamlit as st

subject_list = st.multiselect("意向学科",
  [
    "AI大模型开发",
    "AI智能应用开发",
    "AI嵌入式+机器人开发",
    "AI测试",
    "AI运维"
  ],
  placeholder="请选择意向学科"
)

for subject in subject_list :
  st.write(f"你喜欢{subject}")
```

效果:

![2.7.8 多选下拉框 multiselect效果截图](./Streamlit参考手册-assets/14.png)

#### 2.7.9 滑块 slider

可以使用 `st.slider()` 创建滑块元素。它接收的参数和 `st.number_input()` 差不多，也是可以设置提示语、默认值、最大值、最小值以及步长。

```python
import streamlit as st

# 滑块
temperature = st.slider("模型温度", value=0.8, min_value=0.1, max_value=2.0, step=0.1)

st.write(f"你设定的模型温度是{temperature}")
```

效果:

![2.7.9 滑块 slider效果截图](./Streamlit参考手册-assets/15.png)

#### 2.7.10 按钮 button

使用 `st.button()` 创建按钮。它接收一个字符串作为按钮文本，可以将点击结果赋值给一个变量。

```python
import streamlit as st

submitted = st.button("新建会话")

if submitted:
  st.write(f"新建会话成功啦")
```

效果:

![2.7.10 按钮 button效果截图](./Streamlit参考手册-assets/16.png)

#### 2.7.11 文件上传 file_uploader

`python` 擅长做数据分析，有时候可能需要上传一个 `csv` 之类的文件分析一下。

在 `streamlit` 中可以使用 `st.file_uploader()` 创建一个文件上传元素。

```python
import streamlit as st

# 文件上传
uploaded_file = st.file_uploader("上传文件", type=["csv", "json"])

if uploaded_file:
  st.write(f"你上传的文件是{uploaded_file.name}")
```

`st.file_uploader()` 第一个参数是提示文本，然后可以使用 `type` 属性限制用户上传的文件格式。

接收到的文件可以赋值给一个变量，这个变量接收到文件后可以通过 `.name` 属性查看文件名。

效果:

![2.7.11 文件上传 file_uploader效果截图](./Streamlit参考手册-assets/17.png)

### 2.8 侧边栏 sidebar

使用 `st.sidebar()` 可以给网页弄个侧边栏。

```python
import streamlit as st

with st.sidebar:
  search = st.text_input('搜索：')
  
  st.write(f'页面内容，看看搜索了啥：{search}')
```

效果:

![2.8 侧边栏 sidebar效果截图](./Streamlit参考手册-assets/18.png)

### 2.9 多列布局 columns

按照前面学到的内容写页面的话，所有元素都是从上往下布局的。如果你想一个页面有多列布局，可以使用 `st.columns()` 方法。

```python
import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
  st.write('第1列')

with col2:
  st.write('第2列')

with col3:
  st.write('第3列')
```

效果:

![2.9 多列布局 columns效果截图](./Streamlit参考手册-assets/19.png)

在使用 `st.columns` 时，默认每列的宽度都是一样的。如果你希望每列宽度占比不一样的话可以这样写。

```python
import streamlit as st

# 多列布局（不同比例）
col1, col2, col3 = st.columns([1, 2, 3])

with col1:
  st.write('第1列')

with col2:
  st.write('第2列')

with col3:
  st.write('第3列')
```

此时 `st.columns()` 括号里传入的就不是数字（列数），而是一个数值型列表，这个列表元素个数表示列数，元素的数字表示每列占比。

效果:

![2.9 多列布局 columns效果截图](./Streamlit参考手册-assets/20.png)

### 2.10 选项卡 tabs

使用 `st.tabs()` 可以创建选项卡组件。

```python
import streamlit as st

# 选项卡
tab1, tab2, tab3 = st.tabs(['点赞', '关注', '收藏'])

with tab1:
  st.write('快点赞吧')
with tab2:
  st.write('关注一下啦')
with tab3:
  st.write('收藏就是学会了')
```

效果:

![2.10 选项卡 tabs效果截图](./Streamlit参考手册-assets/21.png)

### 2.11 折叠展开组件 expander

使用 `st.expander()` 可以创建折叠展开组件。

```python
import streamlit as st

with st.expander('更多信息'):
  st.write('传智教育')
  st.write('博学谷')
  st.write('黑马程序员')
```

效果:

![2.11 折叠展开组件 expander效果截图](./Streamlit参考手册-assets/22.png)

### 2.12 扩展：音视频组件

#### 2.12.1 logo

如果你想在页面中，增加一个logo图标，可以使用`st.logo`进行实现。

```python
import streamlit as st

st.logo('./logo.png')
```

效果:

![2.12.1 logo效果截图](./Streamlit参考手册-assets/23.png)

#### 2.12.2 音频标签 audio

```python
import streamlit as st

st.audio('./01.mp3', format='audio/mp3')
```

效果:

![2.12.2 音频标签 audio效果截图](./Streamlit参考手册-assets/24.png)

#### 2.12.3 视频标签 video

```python
import streamlit as st

st.video('./01.mp4', format='video/mp4')
```

效果:

![2.12.3 视频标签 video效果截图](./Streamlit参考手册-assets/25.png)

### 2.13 聊天元素

#### 2.13.1 Chat文本输入框 chat_input

```python
import streamlit as st

prompt = st.chat_input("请输入您想问的问题")
if prompt:
    st.write(f"您输入的问题为: {prompt}")
```

效果:

![2.13.1 Chat文本输入框 chat_input效果截图](./Streamlit参考手册-assets/26.png)

#### 2.13.2 Chat消息 chat_message

```python
import streamlit as st

# 用户信息
with st.chat_message("user"):
    st.write("Hello 👋")
    
# 机器人信息
message = st.chat_message("assistant")
message.write("Hello human")
```

效果:

![2.13.2 Chat消息 chat_message效果截图](./Streamlit参考手册-assets/27.png)
