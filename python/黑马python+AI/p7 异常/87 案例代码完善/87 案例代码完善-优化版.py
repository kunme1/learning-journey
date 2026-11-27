"""来源：87 案例代码完善.py；配套：87 案例代码完善-优化版.md。
整理日期：2026-11-27（北京时间）。原始文件保留；改写理由见就近注释。
"""

# 异常的传递
def fun1():
    print("fun1 ... running ...")
    fun2()


def fun2():
    print("fun2 ... running ...")
    fun3()


def fun3():
    print("fun3 ... running ...")
    print(my_color)


if __name__ == "__main__":
    try: 
        fun1()
    # 本演示刻意使用未定义my_color来观察传播，不把它补成正常变量抹去教学点。
    # 原捕获Exception覆盖范围较宽；已知场景改为NameError，其他类型继续上报。
    except NameError as e:
        print("程序出错了, 请联系管理员 ~ 错误信息: ", e)
