# -------------------- 列表 list 常用方法 --------------------

# 列表定义
s = [56, 90, 88, 65, 90, 100, 209, 72, 145]
print(s)

# append(): 在尾部追加元素
s.append(188)
print(s)

# insert(): 在指定索引之前插入元素
s.insert(2, 80)
print(s)

# remove(): 移除列表中第一个匹配到的元素
s.remove(90)
print(s)

# pop(): 删除列表中指定索引位置的元素（如果未指定则默认最后一个）
# pop():会返回删掉的元素
e = s.pop(1)
print(s)
print(e)

e = s.pop()
print(s)
print(e)

# sort(): 排序
s.sort()
print(s)

# reverse(): 反转列表元素
s.reverse()
print(s)