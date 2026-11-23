"""来源：main.py；配套：学习笔记-优化版.md。
整理日期：2026-11-24；原始文件保留。
"""

# 原main.py：from my_fun import *；import random（未使用）。
# 显式列出实际使用的三个名字，读者能追踪来源，也不受以后__all__变动隐式影响。
# 用的是同目录保留的原my_fun.py；NAME和其他演示函数没有被删除。
from my_fun import PI, log_separator1, log_separator3

# 原顶层直接打印；入口保护使被导入时不打印，直接运行输出保持。
if __name__ == "__main__":
    print(PI)
    log_separator1()
    log_separator3()
