"""来源：69 案例1(递归).py；配套：69 案例1(递归)-优化版.md。
整理日期：2026-11-23；原始练习不修改。
相关改写的原因和行为差异见就近中文说明。
"""

def factorial(n):
    """支持非负整数阶乘；保持递归教学，较大n仍受递归深度限制。"""
    # 原jc缩写不清，factorial是阶乘；原仅n==1导致0/负数无法终止。
    if type(n) is not int or n < 0:
        raise ValueError("n须为非负整数")
    if n <= 1:
        return 1
    # 原else前已有return，可直接写递归返回，逻辑更平直。
    return n * factorial(n - 1)


def factorial_iterative(n):
    """前瞻替代：循环避免递归调用栈；没有做运行速度基准。"""
    if type(n) is not int or n < 0:
        raise ValueError("n须为非负整数")
    result = 1
    for factor in range(2, n + 1):
        result *= factor
    return result


if __name__ == "__main__":
    # 只执行一种实现，避免为对照重复输出；两种实现分别在验证中比较。
    print(factorial(10))
