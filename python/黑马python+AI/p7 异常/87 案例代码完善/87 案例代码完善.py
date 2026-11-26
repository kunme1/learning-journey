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
    except Exception as e:
        print("程序出错了, 请联系管理员 ~ 错误信息: ", e)