"""来源：异常处理.py；配套：86 介绍-优化版.md。
整理日期：2026-11-27（北京时间）。原始文件保留；改写理由见就近注释。
"""

# # 异常处理
# try: 
#     print("====================")
#     print(my_name)
#     print("====================")
# except NameError as e: # 捕获的是 NameError 类型的异常
#     print("程序运行出错, 请联系管理员 ~ 异常信息:", e)


# 原顶层直接演示；函数+入口保护避免导入即执行。
def run_demo():
    # 异常处理
    try: 
        print("====================")
        # print(my_name)
        # print(1 / 0)
        print("ABC"[10])
        # print("ABC".hello)
        print("====================")
    except NameError as e: # 捕获的是 NameError 类型的异常
        print("名字不存在, 请检查变量或函数名字, 异常信息:", e)
    except ZeroDivisionError as e:
        print("0不能做除数,异常信息:", e)
    except IndexError as e:
        # 原活动表达式是"ABC"[10]，原先只捕获NameError／ZeroDivisionError，接不住它。
        # 补IndexError后打印提示再执行finally，不再把预期的索引演示作为未处理异常抛出。
        print("索引错误,异常信息:", e)
    # except Exception as e: # 捕获所有异常
    #     print("程序运行出错了, 请联系管理员, 错误信息: ", e)
    finally:
        # finally展示扫尾执行时机；本例没有打开真实资源，print不等于完成了资源释放。
        print("资源释放 ~")

if __name__ == "__main__":
    run_demo()
