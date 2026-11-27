# 写文件


# # ======================= 释放资源方式一: =======================
# # 1.打开文件
# f= open("D:/专业技能/learning-journey/python/黑马python+AI/p8 AI应用/100-119 实战/109-117 会话管理/110 文件操作入门/静夜思.txt", "w",  encoding="utf-8" )

# # 2.写入文件内容
# try: 
#     f.write("静夜思(李白)\n\n")
#     f.write("床前明月光\n")
#     i = 1 / 0
#     f.write("疑似地上霜\n")
#     f.write("举头望明月\n")
#     f.write("低头思故乡\n")
# finally:
#     print("文件已关闭")
#     # 3.关闭文件
#     f.close()


# ======================= 释放资源方式二(最佳实践): =======================
# 1.打开文件
with open("D:/专业技能/learning-journey/python/黑马python+AI/p8 AI应用/100-119 实战/109-117 会话管理/110 文件操作入门/静夜思.txt", "w",  encoding="utf-8" ) as f:  
    # 2.写入文件内容
    f.write("静夜思(李白)\n\n")
    f.write("床前明月光\n")
    i = 1 / 0
    f.write("疑似地上霜\n")
    f.write("举头望明月\n")
    f.write("低头思故乡\n")
    print("文件已关闭")
    # 3.关闭文件
    f.close()
