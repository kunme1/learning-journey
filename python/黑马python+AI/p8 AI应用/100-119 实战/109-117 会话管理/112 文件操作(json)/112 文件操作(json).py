import json

# 写入json数据文件
user = {
    "name": "张三",
    "age": 18,
    "gender": "男",
    "hobby": ["看电影", "听音乐", "看小说"]
}

with open("D:/专业技能/learning-journey/python/黑马python+AI/p8 AI应用/100-119 实战/109-117 会话管理/112 文件操作(json)/user.json", "w", encoding="utf-8") as f:  # 创建json文件
    # ensure_ascii: 默认为True，确保输出的json数据是ASCII编码(非ASCII编码的会转成ASCII编码); False: 非ASCII编码的会保持不变
    # indent: 会在输出的json数据中添加缩进(格式化)
    json.dump(user, f, ensure_ascii=False, indent = 2)


# 读取json数据文件
with open("D:/专业技能/learning-journey/python/黑马python+AI/p8 AI应用/100-119 实战/109-117 会话管理/112 文件操作(json)/user.json", "r", encoding="utf-8") as f:  # 创建json文件
    user = json.load(f)
    print(user)
    print(type(user))