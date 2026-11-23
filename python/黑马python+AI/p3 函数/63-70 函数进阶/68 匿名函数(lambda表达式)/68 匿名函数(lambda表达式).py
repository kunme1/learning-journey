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