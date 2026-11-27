# 95 Apifox接口测试（优化版）

> 整理日期：2026-11-27（北京时间）；截止／首次扫描：2026-11-27T04:36:38+08:00。采用首次读取快照，无法还原消息发送瞬间文件。课节首次学习日期未完整登记，历史资料补齐，原学习日期未确认；当天问答日期另据共享记录标注。
> 来源：[95 Apifox接口测试.py](<95 Apifox接口测试.py>)；[95 Apifox接口测试.md](<95 Apifox接口测试.md>)。原笔记、代码和图片保留；补充不表示用户已掌握或运行。


![原图 image.png](<image.png>)

**图片文字版（来源：image.png）：**

Apifox为API设计、开发、测试协作工具。图中功能关系：API设计／接口文档为核心，连接API开发调试、API Mock、API文档分享、API自动化测试。

原笔记“浏览器地址栏发起get，提示词大只能post”需区分：普通地址栏导航通常GET，网页脚本／表单也能POST；此接口用POST首先因为服务契约要求，并非所有AI协议都只因体积大才POST。


![原图 image-1.png](<image-1.png>)

**图片文字版（来源：image-1.png）：**

课件旧版DeepSeek文档与curl调用：URL `https://api.deepseek.com/chat/completions`；请求头Content-Type: application/json、Authorization: Bearer ${DEEPSEEK_API_KEY}；请求体model/messages/stream。旧示例结构：
```json
{
  "model": "deepseek-chat",
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful assistant."
    },
    {
      "role": "user",
      "content": "Hello!"
    }
  ],
  "stream": false
}
```

图中旧模型名仅作为当时文档，当前源码名称按本次官方文档核对。


![原图 image-2.png](<image-2.png>)

**图片文字版（来源：image-2.png）：**

JSON：对象用{}、数组用[]、字符串和键用双引号、数字如12和3.14、布尔true/false。图内完整请求：
```json
{
  "model": "deepseek-chat",
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful assistant."
    },
    {
      "role": "user",
      "content": "Hello!"
    }
  ],
  "stream": false
}
```

补齐null是JSON类型之一；“值可以任意类型”应限定为JSON支持的类型，不包括任意Python对象。


![原图 image-3.png](<image-3.png>)

**图片文字版（来源：image-3.png）：**

用户Apifox截图为POST同一官方端点，Body JSON如下：
```json
{
  "model": "deepseek-flash",
  "messages": [
    {
      "role": "system",
      "content": "你是一名非常可爱的AI助理，你的名字叫小甜甜，请你使用温柔可爱的语气回答用户的问题。"
    },
    {
      "role": "user",
      "content": "你是谁"
    }
  ],
  "thinking": {
    "type": "enabled"
  },
  "reasoning_effort": "high",
  "stream": false
}
```

可见HTTP200，返回chat.completion、choices[0].message.role=assistant、content为小甜甜自我介绍，另有reasoning_content、finish_reason=stop；usage为prompt_tokens=53、completion_tokens=77、total_tokens=130，reasoning_tokens=35、cached_tokens=0。请求头只显示Headers 2，具体键值不可见，不能据此确认实际密钥。响应ID／时间戳及冗长生成修辞不影响本课结构，文字版省略。

**今日纠错：**405截图当时用GET，官方Chat Completions要求POST；当前图已POST并显示200，两阶段不混同。JSON数组元素用半角逗号，全角逗号仅能在字符串内作普通文字。当前官方契约接受deepseek-flash、thinking.enabled和reasoning_effort=high，不按旧图把它们判错。[DeepSeek接口契约](https://api-docs.deepseek.com/api/create-chat-completion/)。


![原图 image-4.png](<image-4.png>)

**图片文字版（来源：image-4.png）：**

system消息设定人设／风格／行为规则，user消息包含实际问题。图中system设名小甜甜、亲切可爱回答；user问“你是谁”。角色是消息字段值，不是Python类。

### 原始代码：[95 Apifox接口测试.py](<95 Apifox接口测试.py>)

原文件为空，本目录无活动代码可评审，不虚构执行结果。


## 代码、命名与效率检查

原本地脚本为空，知识来自原图／原.md及课程对应小节；未虚构本地执行或已掌握。无须为固定概念笔记制造Python优化版。

|原名|建议／保留|中文含义|位置|原因|
|---|---|---|---|---|
|课件术语／示例名|保留或按就近纠正|概念与示例|对应原图|没有活动Python标识符命名问题；需纠正的英文／参数拼写在正文注明|

检查含拼写、语义、缩写、大小写／下划线、单位和内置名遮蔽。除已列项，未发现需要修改的问题；合法教学名／样本值保留。未测性能，不把更短说成更快。


## 参考与补漏

本次实际对照下载课程BV1sHU9BmEne对应小节；Video2Book二次资料不是绝对答案，补漏／纠正已放到相关知识点旁。没有观看原视频，不把参考包整册算作用户已学。

- [模块17_AI应用：大模型部署、网络协议与API调用_精读全书.md](<../../../../../../参考资料/黑马Python-AI课程笔记/计算机/编程语言/黑马程序员-Python-AI/textbooks/模块17_AI应用：大模型部署、网络协议与API调用_精读全书.md>)：P95，818—1018行：接口测试、JSON与参数。
- [笔记09_AI应用大模型部署网络协议与API调用_笔记.md](<../../../../../../参考资料/黑马Python-AI课程笔记/计算机/编程语言/黑马程序员-Python-AI/notes/笔记09_AI应用大模型部署网络协议与API调用_笔记.md>)：424—497行，客户端和契约。

