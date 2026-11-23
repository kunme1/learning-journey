# 导入模块 ---> 调用方式: 模块名.功能名 / 别名.功能名
# import random
# import random as rd

# for i in range(100):
#     print(rd.randint(1, 100))

# 导入模块中的功能from ... import ... ---> 调用方式: 功能名 / 别名 ---> *:通配符
from random import randint as rd
# from random import randint
# from random *
print(rd(1, 100))



