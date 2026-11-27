# 97 本地DeepSeek（优化版）

> 整理日期：2026-11-27（北京时间）；截止／首次扫描：2026-11-27T04:36:38+08:00。采用首次读取快照，无法还原消息发送瞬间文件。课节首次学习日期未完整登记，历史资料补齐，原学习日期未确认；当天问答日期另据共享记录标注。
> 来源：[97 本地DeepSeek.py](<97 本地DeepSeek.py>)；[97 本地DeepSeek.md](<97 本地DeepSeek.md>)。原笔记、代码和图片保留；补充不表示用户已掌握或运行。


![原图 image.png](<image.png>)

**图片文字版（来源：image.png）：**

本机命令行 `ollama run deepseek-r1:8b`，随后出现 `>>> Send a message (/? for help)`。说明CLI交互已启动，不据此推断每次HTTP请求会自动带历史。


![原图 image-1.png](<image-1.png>)

**图片文字版（来源：image-1.png）：**

本地接口POST `http://localhost:11434/api/chat`；图中复制了官方请求的thinking和reasoning_effort字段：
```json
{
  "model": "deepseek-r1:8b",
  "messages": [
    {
      "role": "system",
      "content": "你是一名非常可爱的AI助理，你的名字叫小言言，请你使用温柔可爱的语气回答用户的问题。"
    },
    {
      "role": "user",
      "content": "我现在有12个苹果，3个人，怎么均分？"
    }
  ],
  "thinking": {
    "type": "enabled"
  },
  "reasoning_effort": "high",
  "stream": false
}
```

这里是图中原样参数，原生Ollama契约与官方DeepSeek不同，正确最小参数见下方纠正。

**纠正：**Ollama原生/api/chat用其自己的参数；图中的thinking对象／reasoning_effort来自另一服务，200不证明它们有作用。最小请求可去掉它们；如需控制思考，核对模型支持的原生think。原生非流式响应取message.content，官方SDK取choices[0].message.content，路径不同。[Ollama聊天API](https://docs.ollama.com/api/chat)。


![原图 image-2.png](<image-2.png>)

**图片文字版（来源：image-2.png）：**

同一请求成功截图200；原生响应核心：model=deepseek-r1:8b、message.role=assistant、message.content回答12÷3=4、message.thinking另列、done=true、done_reason=stop。图中指标total_duration=14999116900、load_duration=6341082200、prompt_eval_count=42、prompt_eval_cached_count=0、prompt_eval_duration=336227000、eval_count=277、eval_duration=8311183999，时长单位为纳秒。模型长篇修辞与中间推理不逐句复写；结构和结论保留，不把图中15s当成本批测速。


![原图 image-3.png](<image-3.png>)

**图片文字版（来源：image-3.png）：**

仅把user替换为“两个人呢？”而没有苹果历史；本地服务200，content转为对“两个人”关系的泛化回答而不是均分计算。done=true，输入token31、缓存27、输出254、total_duration=7475696900（纳秒）。这不能作为跨请求带会话记忆的证据；缓存命中与应用历史是不同概念。


![原图 image-4.png](<image-4.png>)

**图片文字版（来源：image-4.png）：**

messages加入第一次user苹果问题、assistant每人4个，再追加user“2个人呢？”；图示回答12÷2=6。响应message包含content与thinking，done=true，输入149、缓存27、输出330；total_duration=9493474800（纳秒）。文本结构转写省略冗长人设修辞：
```json
{
  "model": "deepseek-r1:8b",
  "messages": [
    {
      "role": "system",
      "content": "你是一名非常可爱的AI助理，你的名字叫小甜甜，请你使用温柔可爱的语气回答用户的问题。"
    },
    {
      "role": "user",
      "content": "我现在有12个苹果，3个人，怎么均分？"
    },
    {
      "role": "assistant",
      "content": "12个苹果分给3个人，每个人4个。"
    },
    {
      "role": "user",
      "content": "那两个人呢？"
    }
  ],
  "stream": false
}
```

截图未展示当前请求thinking参数是否真的生效，不能由200反推每个多余字段都被支持。

原笔记“本地模型也没有上下文记忆”在这些独立HTTP请求中成立：仍要发送历史。CLI能连续对话，是客户端替你维护上下文；服务不自动按同一机器识别上一问。原生接口默认stream=true，初学抓整包时显式false，不将其默认与官方接口混为一谈。

### 原始代码：[97 本地DeepSeek.py](<97 本地DeepSeek.py>)

原文件为空，本目录无活动代码可评审，不虚构执行结果。


## 代码、命名与效率检查

原本地脚本为空，知识来自原图／原.md及课程对应小节；未虚构本地执行或已掌握。无须为固定概念笔记制造Python优化版。

|原名|建议／保留|中文含义|位置|原因|
|---|---|---|---|---|
|课件术语／示例名|保留或按就近纠正|概念与示例|对应原图|没有活动Python标识符命名问题；需纠正的英文／参数拼写在正文注明|

检查含拼写、语义、缩写、大小写／下划线、单位和内置名遮蔽。除已列项，未发现需要修改的问题；合法教学名／样本值保留。未测性能，不把更短说成更快。


## 参考与补漏

本次实际对照下载课程BV1sHU9BmEne对应小节；Video2Book二次资料不是绝对答案，补漏／纠正已放到相关知识点旁。没有观看原视频，不把参考包整册算作用户已学。

- [模块17_AI应用：大模型部署、网络协议与API调用_精读全书.md](<../../../../../../参考资料/黑马Python-AI课程笔记/计算机/编程语言/黑马程序员-Python-AI/textbooks/模块17_AI应用：大模型部署、网络协议与API调用_精读全书.md>)：P97，1192—1320行：Ollama聊天接口。
- [笔记09_AI应用大模型部署网络协议与API调用_笔记.md](<../../../../../../参考资料/黑马Python-AI课程笔记/计算机/编程语言/黑马程序员-Python-AI/notes/笔记09_AI应用大模型部署网络协议与API调用_笔记.md>)：548—570行，本地接口。

