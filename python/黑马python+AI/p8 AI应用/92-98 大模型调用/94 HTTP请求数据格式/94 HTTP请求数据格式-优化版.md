# 94 HTTP请求数据格式（优化版）

> 整理日期：2026-11-27（北京时间）；截止／首次扫描：2026-11-27T04:36:38+08:00。采用首次读取快照，无法还原消息发送瞬间文件。课节首次学习日期未完整登记，历史资料补齐，原学习日期未确认；当天问答日期另据共享记录标注。
> 来源：[94 HTTP请求数据格式.py](<94 HTTP请求数据格式.py>)；[94 HTTP请求数据格式.md](<94 HTTP请求数据格式.md>)。原笔记、代码和图片保留；补充不表示用户已掌握或运行。


![原图 image.png](<image.png>)

**图片文字版（来源：image.png）：**

HTTP/1.1请求行、请求头、空行、请求体的截图转写：
```http
POST /api/courses HTTP/1.1
Accept: application/json, text/plain, */*
Accept-Encoding: gzip, deflate, br, zstd
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Connection: keep-alive
Content-Length: 139
Content-Type: application/json
Host: localhost:90
Origin: http://localhost:90
Referer: http://localhost:90/resource/course
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/143.0.0.0

{"phone":"18808088080","channel":1,"name":"虎咆","gender":1,"age":"32"}
```

这是截图分区内容；Content-Length为图中139，截图body可能是节选，不能把这两者作为重新发送时可复用的长度。图写GET无请求体、POST大小无限制，下方作边界纠正。示例查询 `/api/courses?name=Python&status=1` 用?和&组织参数。

**纠正：**GET请求内容没有通用定义，不应依赖GET正文互通，不是语法绝对不能存在。POST也受服务器、网关与接口大小限制；查询参数并非GET独占，POST也可有URL参数。Content-Length按编码后**字节**计，不是字符数，交给客户端库生成。[HTTP语义](https://httpwg.org/specs/rfc9110.html#GET)。


![原图 image-1.png](<image-1.png>)

**图片文字版（来源：image-1.png）：**

响应分为状态行、响应头、空行、响应体。图示：
```http
HTTP/1.1 200
Server: nginx/1.24.0
Date: Tue, 16 Dec 2025 12:38:08 GMT
Content-Type: application/json
Transfer-Encoding: chunked
Connection: keep-alive

{code: 1, msg: "success", data: null}
```

截图body是开发工具样式，键没引号，若写成原始JSON须加双引号。状态码图例200成功、400请求参数错误、404资源不存在、500服务端错误；不据200单独判断业务一定成功。

**补充：**HTTP状态和JSON内业务code是两层；200表示HTTP请求成功语义，仍需核对业务字段和回答。405优先检查方法，401检查鉴权，不能把Missing credentials等客户端构造错误直接叫HTTP401。


![原图 image-2.png](<image-2.png>)

**图片文字版（来源：image-2.png）：**

小结：请求为请求行（方法／路径）、请求头key:value、可选请求体；响应为状态行、响应头key:value、响应体。重点记忆200、400、404、500及各自诊断方向。

### 原始代码：[94 HTTP请求数据格式.py](<94 HTTP请求数据格式.py>)

原文件为空，本目录无活动代码可评审，不虚构执行结果。


## 代码、命名与效率检查

原本地脚本为空，知识来自原图／原.md及课程对应小节；未虚构本地执行或已掌握。无须为固定概念笔记制造Python优化版。

|原名|建议／保留|中文含义|位置|原因|
|---|---|---|---|---|
|课件术语／示例名|保留或按就近纠正|概念与示例|对应原图|没有活动Python标识符命名问题；需纠正的英文／参数拼写在正文注明|

检查含拼写、语义、缩写、大小写／下划线、单位和内置名遮蔽。除已列项，未发现需要修改的问题；合法教学名／样本值保留。未测性能，不把更短说成更快。


## 参考与补漏

本次实际对照下载课程BV1sHU9BmEne对应小节；Video2Book二次资料不是绝对答案，补漏／纠正已放到相关知识点旁。没有观看原视频，不把参考包整册算作用户已学。

- [模块17_AI应用：大模型部署、网络协议与API调用_精读全书.md](<../../../../../../参考资料/黑马Python-AI课程笔记/计算机/编程语言/黑马程序员-Python-AI/textbooks/模块17_AI应用：大模型部署、网络协议与API调用_精读全书.md>)：P94，615—755行：请求响应与状态。
- [笔记09_AI应用大模型部署网络协议与API调用_笔记.md](<../../../../../../参考资料/黑马Python-AI课程笔记/计算机/编程语言/黑马程序员-Python-AI/notes/笔记09_AI应用大模型部署网络协议与API调用_笔记.md>)：319—408行，报文结构。

