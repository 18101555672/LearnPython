# time库的使用
import time

# 时间获取
# time() 获取当前时间戳，即计算机内部时间值，浮点数
print(time.time())
# ctime() 获取当前时间并以易读方式表示，返回字符串
print(time.ctime())
# gmtime() 获取当前时间，表示为计算机可处理的时间格式
print(time.gmtime())

# 时间格式化
# strftime(tpl,ts)
# tpl是格式化模板字符串，用来定义输出效果
# ts是计算机内部时间类型变量,ts无法使用time.ctime()和time.time()
t = time.strftime('%Y-%m-%d %H:%M:%S',time.gmtime())
print(t)
# strptime(str,tpl)
# str是字符串形式的时间值
# tpl是格式化模板字符串，用来定义输入效果
print(time.strptime(t,'%Y-%m-%d %H:%M:%S'))
# %Y 年份 0000-9999
# %m 月份 01-12
# %B 月份名称 January-December
# %b 月份名称缩写 Jan-Dec
# %d 日期 01-31
# %A 星期 Monday-Sunday
# %a 星期缩写 Mon-Sun
# %H 24小时制 00-23
# %h 12小时制 01-12
# %p 上,下午 AM,PM
# %M 分钟 00-59
# %S 秒数 00-59

# 程序计时应用
# perf_counter() 返回一个CPU级别的精确时间计数值，单位为秒
# 由于这个计数值起点不确定，连续调用差值才有意义
print(time.perf_counter())
print(time.perf_counter())
# sleep(s) s拟程序休眠的时间，单位是秒，可以是浮点数
time.sleep(2)
print(time.perf_counter())
