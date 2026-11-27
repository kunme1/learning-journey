from datetime import datetime
print(datetime.now())
# %Y-%m-%d %H:%M:%S: %Y - 年 %m - 月 %d - 日 %H:%M:%S - 时:分:秒
dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(dt)