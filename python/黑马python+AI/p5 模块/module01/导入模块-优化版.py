"""来源：导入模块.py；配套：学习笔记-优化版.md。
整理日期：2026-11-24；原始文件保留。
"""

# 原活动语句：from random import randint as rd；print(rd(1, 100))。
# rd合法，但在本课另一注释中又代表random模块，容易混淆对象种类。
# 改为直接使用randint，名称就是“随机整数”；端点仍均包含，不改变随机范围。
from random import randint

print(randint(1, 100))
# 比较语法仍可写在原文件注释中；不把全部形式同时运行造成多次随机输出。
