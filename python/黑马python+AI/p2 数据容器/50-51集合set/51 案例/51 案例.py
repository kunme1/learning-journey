# 选修足球学生名单
football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}

# 选修篮球学生名单
basketball_set = {"张铁", "墨居仁", "王林", "姜老道", "曾牛", "王婵", "韩立", "天运子", "李化元", "厉飞雨", "云露"}

# 选修法语学生名单
french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子", "红蝶", "厉飞雨", "韩立", "曾牛"}

# 选修艺术学生名单
art_set = {"遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}

# 1. 找出同时选修了法语和艺术的学生

# 方式1
fa_set = french_set.intersection(art_set)
print(f"同时选修了法语和艺术的学生: {fa_set}")

# 方式2 : & ---> 求交集
fa_set2 = french_set & art_set
print(f"同时选修了法语和艺术的学生: {fa_set2}")

# 2. 找出同时选修了所有四门课程的学生
all_set = french_set & basketball_set & french_set & art_set
print(f"同时选修了所有四门课程的学生: {all_set}")

# 3. 找出选修了足球, 但是没有选修篮球的学生
fb_set = football_set - basketball_set
print(f"选修了足球, 但是没有选修篮球的学生: {fb_set}")

fb_set1 = football_set.difference(basketball_set)
print(f"选修了足球, 但是没有选修篮球的学生: {fb_set1}")

# 方式三：集合推导式 ---> 快速构建集合，语法：{要往集合中添加的数据 for s in set1 if 条件}
fb_set2 = { s for s in football_set if s not in basketball_set}
print(f"选修了足球, 但是没有选修篮球的学生: {fb_set2}")

# 4. 统计每一个学生选修的课程数量 -- 并集 (|)
# 4.1 获取学生名单
stu = football_set | basketball_set | french_set | art_set
print(stu)

# 4.2 获取每一个学生选修的课程数量
all_list = [*football_set, *basketball_set, *french_set, *art_set]

for s in stu:
    print(f"学生{s}选修了{all_list.count(s)}门课程")