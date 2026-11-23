# # 导入模块,会执行模块中非函数体的代码
# import my_fun as mf

# # 使用模块中的功能
# mf.log_separator1()

# print(mf.PI)
# print(mf.NAME)

# 导入自定义模块中的功能
# from my_fun import log_separator1,log_separator3,PI,NAME
from my_fun import *
import random

# 使用模块中的功能
print(PI)

log_separator1()
# log_separator2()
log_separator3()
# log_separator4()