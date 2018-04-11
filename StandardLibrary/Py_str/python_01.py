# 字符串操作
# 字符串属性方法操作：
s = 'Python stRING'
# 1.字符串格式输出对齐
# 中间对齐
print(s.center(20))
# 左对齐
print(s.ljust(20))
# 右对齐
print(s.rjust(20))

# 2.大小写转换
# 转大写
print(s.upper())
# 转小写
print(s.lower())
# 首字母转大写
print(s.capitalize())
# 大小写对转
print(s.swapcase())
# 以分隔符为标记，首字母大写，其余小写
print(s.title())
s = 'pYthon-sTRing'
print(s.title())

# 3.字符串条件判断
# isalnum()是否全是字母和数字，并至少有一个字符
# isdigit()是否全是数字，并至少有一个字符
# isalpha()是否全是字母，并至少有一个字符
# islower()是否全是小写，当全是小写字母和数字一起时候，也返回True
# isupper()是否全是大写，当全是大写字母和数字一起时候，也返回True
# istitle()是否所有单词首字母都是大写
# startswith(x)是否以字符串x开头
# endswith(x)  是否以字符串x结尾

# 4.字符串搜索定位与替换
# find(s) 查找字符串s，没有则返回-1，有则返回第一个匹配的索引
# rfind(s) 查找字符串s，没有则返回-1，有则返回最后一个匹配的索引
# index(s) 查找字符串s，没有则报错，有任返回第一个匹配的索引
# rindex(s) 查找字符串s，没有则报错，有任返回最后一个匹配的索引
# count(s) 统计字符串s匹配的次数
# replace(x,y) 替换匹配，将所有匹配到的x替换成y
# strip(s) 删除字符串收尾匹配的字符s，通常用于默认删除回车符
# lstrip(s) 删除字符串首匹配的字符s
# rstrip(s) 删除字符串首匹配的字符s
# expandtabs(n) 将制表符转为空格，n为指定空格数，默认为8
s = '\tab'
print(s.expandtabs())
print(s.expandtabs(0))
print(s.expandtabs(1))

# 5.字符串分割变换
str = 'Learn string'
li = ['Learn','string']
tup = ('Learn','string')
# x.join(s) 将字符x插入s中(s可以是字符串，列表,元祖)
print('-'.join(str))
print('-'.join(li))
print('-'.join(tup))
# split(s,n) 从首开始以字符s分割字符串，n是分割次数，可不填，则分割全部
print(str.split('n'))
print(str.split('n',1))
# rsplit(s,n) 从尾开始以字符s分割字符串，n是分割次数，可不填，则分割全部
print(str.rsplit('n'))
print(str.rsplit('n',1))