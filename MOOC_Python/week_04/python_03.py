# encoding=utf-8
# 程序的循环结构

# 遍历循环
for i in range(5):
    print(i)
for c in 'hello':
    print(c)
for item in [1,2,3,'a','b']:
    print(item)

# 无限循环
a = 3
while a > 0:
    a -= 1
    print(a)

# 循环控制保留字
# break跳出并结束当前整个循环，执行循环后的语句
# continue结束档次循环，继续执行后续次数循环
# break和continue可以与for和while循环搭配使用
# 一个break或continue只能跳出一个循环

# 循环高级用法
for i in range(2):
    print(i)
else:
    print('hi')
# 当循环没有被break语句退出时，执行else语句块
# else语句块作为正常完成循环的奖励
# 循环中的else用法与异常处理中的else用法相似