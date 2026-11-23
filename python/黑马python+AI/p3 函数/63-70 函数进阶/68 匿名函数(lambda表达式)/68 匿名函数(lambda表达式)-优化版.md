# 68 匿名函数(lambda表达式)（优化版）

> 整理日期：2026-11-23（北京时间）；本批截止／首次读取快照：2026-11-23T15:54:33+08:00。历史资料补齐，原学习日期未确认。相关问答按共享记录的11月22日／23日分别列入日报，不把这些课节全记为今日新学。
> 来源：[68 匿名函数(lambda表达式).py](<68 匿名函数(lambda表达式).py>)；[68 匿名函数(lambda表达式).md](<68 匿名函数(lambda表达式).md>)。原始文件保留，下面“补充／纠正／前瞻优化”是整理说明，不表示用户已掌握或执行。


### lambda表达式

![原图 image.png](<image.png>)

**图片文字版（来源：image.png）：**



```python
def out_line():
    print("-------------------------------")

def add(x, y):
    return x + y

# 相应lambda示例：
out_line = lambda: print("-------------------------------")
add = lambda x, y: x + y
out_line()
print(add(100, 200))
```

语法lambda 参数列表: 表达式；适用于短逻辑，常用作函数参数。

**纠正（教材／复习笔记）：**lambda体是一个表达式，不是必须物理一行；括号内可折行。无需先赋给变量才可用，(lambda x:x+1)(2)即可；lambda:print(...)也返回None，不是没有任何返回值。命名函数与lambda并不以是否能返回区分。当前add(100,200)已经调用但未print，返回300未显示；不是调用失败。

**对应原始代码片段（保留注释状态）：**

```python
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
```



### 何时用匿名／命名函数

![原图 image-1.png](<image-1.png>)

**图片文字版（来源：image-1.png）：**

简单、单处作为回调时可用lambda；多步骤、多处复用或需文档时用def。图强调可读性、可维护性比简短重要。

当前按长度排序的lambda item:len(item)可等价简写key=len，item是形参不是关键字，lambda才是关键字，key是接口定义的参数名。sort对每个元素调用一次key，保存键用于比较，不把原元素替换为长度；等长保持原相对顺序。题干要求从短到长，当前reverse=True实际从长到短，优化版按题干去掉它；若是刻意练习降序，原行合法可保留。官方签名sort(*, key=None, reverse=False)，*表示仅限关键字，不是让你填写值。图中编辑器官方文档超链接不保证每个IDE都有；11月23日参数提示已保存项目设置，真实悬浮效果未确认。

**对应原始代码片段（保留注释状态）：**

```python
# 需求3：完成如下列表的排序操作，按照每一个元素的字符个数，从小到大排序；

data_list = ["C++", "C", "Python", "Jack", "PHP", "Java", "Go", "JavaScript", "Rust"]
print(data_list)


# 匿名函数典型的应用场景:作为方法调用的参数 or 高阶函数调用的参数来传递,
data_list.sort(key = lambda item : len(item), reverse=True)# sort是把列表中的每个元素作为参数，传给 key 指定的匿名函数。按照返回值的大小再排序,大小相同的按照原来的顺序
print(data_list)
```


### Python优化版对照：68 匿名函数(lambda表达式).py

key=lambda item:len(item)可简写key=len；当前reverse=True是降序，与题干升序相反，优化版按题干调整。 配套文件：[68 匿名函数(lambda表达式)-优化版.py](<68 匿名函数(lambda表达式)-优化版.py>)。

等价部分仅为key=len替代转发lambda；排序方向按题干改成升序是行为变化。lambda是定义匿名函数的关键字、item为形参；sort负责传入每个元素。



```python
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
```

以上是完整可独立运行的建议文件；原源码见相邻原始片段和文末备查。


## 代码检查、命名与实际输出

key=lambda item:len(item)可简写key=len；当前reverse=True是降序，与题干升序相反，优化版按题干调整。

|原名|建议|中文含义|文件位置|原因|
|---|---|---|---|---|
|item、key、len|item可变；key/len保留|形参／接口参数／长度函数|sort调用|item不是关键字；lambda才是，key不能随意改|
|out_line/add|保留|分割线与加法匿名函数|语法对照|不删除课程对照|


对应Python文件已经同步原写法、改写原因与行为差异。改名／更短不自动等于更快；具体收益与限制见相应案例附近，没有做性能基准。

**原文件实际运行输出（68 匿名函数(lambda表达式).py；模拟输入／受控捕获）：**

```text
------------------------------------
['C++', 'C', 'Python', 'Jack', 'PHP', 'Java', 'Go', 'JavaScript', 'Rust']
['JavaScript', 'Python', 'Jack', 'Java', 'Rust', 'C++', 'PHP', 'Go', 'C']
```


## 完整原始源码备查

正文按原知识点顺序保留图文，并在相关案例附近解释代码；下方逐文件保留完整原始代码（含学习注释），不激活已注释片段。

### [68 匿名函数(lambda表达式).py](<68 匿名函数(lambda表达式).py>)


```python
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
data_list.sort(key = lambda item : len(item), reverse=True)# sort是把列表中的每个元素作为参数，传给 key 指定的匿名函数。按照返回值的大小再排序,大小相同的按照原来的顺序
print(data_list)
```


## 参考与补漏

本次实际对照以下对应小节；资料为Video2Book二次整理，不把后续整册内容计作本课遗漏。具体补漏／纠正已经放在知识点附近。

- [模块11_函数进阶：作用域、传参机制与 lambda 匿名函数_精读全书.md](<../../../../../../参考资料/黑马Python-AI课程笔记/计算机/编程语言/黑马程序员-Python-AI/textbooks/模块11_函数进阶：作用域、传参机制与 lambda 匿名函数_精读全书.md>)：P68，本次实际读取的对应段落，695—855行。
- [笔记06_函数体系与类型注解作用域传参机制与 lambda_笔记.md](<../../../../../../参考资料/黑马Python-AI课程笔记/计算机/编程语言/黑马程序员-Python-AI/notes/笔记06_函数体系与类型注解作用域传参机制与 lambda_笔记.md>)：467—524行，对应复习小节。

原始材料与参考资料保持只读；本稿新增示例的运行边界见代码检查。
