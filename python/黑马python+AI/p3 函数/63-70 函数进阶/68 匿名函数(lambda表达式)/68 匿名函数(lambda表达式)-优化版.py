"""来源：68 匿名函数(lambda表达式).py；配套：68 匿名函数(lambda表达式)-优化版.md。
整理日期：2026-11-23；原始练习不修改。
相关改写的原因和行为差异见就近中文说明。
"""

# 需求1: 打印分割线
# def out_line():
#     print("------------------------------------")

out_line = lambda: print("------------------------------------")
out_line()


# 需求2：计算两个数之和

# def add(x, y):
#     return x + y

add = lambda x, y: x + y
add(100, 200)

# 需求3：完成如下列表的排序操作，按照每一个元素的字符个数，从小到大排序；

data_list = ["C++", "C", "Python", "Jack", "PHP", "Java", "Go", "JavaScript", "Rust"]
print(data_list)


# 匿名函数典型的应用场景:作为方法调用的参数 or 高阶函数调用的参数来传递,
# 原lambda item: len(item)仅转发len，可直接传key=len，元素和稳定性不变。
# 原reverse=True为长到短；按题干“从小到大”去掉它，属于排序方向的行为变化。
# key和reverse仅能以关键字传入，len不加()，sort自行逐元素调用。
data_list.sort(key=len)# sort是把列表中的每个元素作为参数，传给 key 指定的匿名函数。按照返回值的大小再排序,大小相同的按照原来的顺序
print(data_list)
