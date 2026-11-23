"""来源：51 案例.py；配套：51 案例-优化版.md。
整理日期：2026-11-23；原始练习不修改。
相关改写的原因和行为差异见就近中文说明。
"""

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
# 错误修复：原式重复french_set，漏football_set，会误纳入姜老道。
all_set = football_set & basketball_set & french_set & art_set
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

# 4.2 原写法摊平为all_list，再为每个学生count，会反复扫描整表。
# 改后：对四个课程集合各判断一次成员关系，True按1累加。
# 新语法：生成器表达式交给sum逐项消费；不创建完整重复姓名列表。
# 计数值不变；集合输出和遍历仍无顺序保证，不声称实测更快。
courses = (football_set, basketball_set, french_set, art_set)
for student in stu:
    course_count = sum(student in course for course in courses)
    print(f"学生{student}选修了{course_count}门课程")
