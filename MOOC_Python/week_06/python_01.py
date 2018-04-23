# encoding=utf-8
# 集合类型及操作
# 集合是多个唯一元素的无序组合
# 集合用大括号{}表示，元素间用逗号,分隔
# 建立集合用{}或set()
s1 = {1,2,'hi',(1,8)}
s2 = set('12das13')
# 建立空集合只能使用set()
s3 = set()

# 集合操作符
# | 并集  返回两个集合中的所有元素
# - 差集  返回在集合1但不在集合2中的元素
# & 交集  返回同时在两个集合中的元素
# ^ 补集  返回两个集合中非相同的元素
# <=或<   判断子集关系，返回True/False
# >=或>   判断包含关系，返回True/False
# python增强操作符
# |= 更新集合1，包括在集合1和集合2中的所有元素
# -= 更新集合1，包括在集合1但不在集合2中的元素
# &= 更新集合1，包括同时在集合1和集合2中的元素
# ^= 更新集合1，包括集合1和集合2中非相同的元素
a = {'p','y',123}
b = set('pypy123')
print(a)
print(b)
print(a-b)
print(b-a)
print(a&b)
print(a|b)
print(a^b)

# 集合处理方法
# s.add(x) 如果x不在集合S中，将x增加到S
# s.discard(x) 移除s中的元素x，如果x不在集合s中，不会报错
# s.remove(x) 移除s中的元素x，如果x不在集合s中，产生KeyError异常
# s.clear(x) 移除s中所有的元素
# s.pop(x) 随机移除并返回s中的一个元素，并更新s，若s为空则产生KeyError异常
# s.copy() 返回集合s的一个副本
# len(s) 返回集合s的元素个数
# x in s 判断元素x是否在集合s中，是则返回True，否则返回False
# x not in s 判断元素x是否在集合s中，否则返回True，是则返回False
# set(x) 将其他类型变量x转变为集合类型

# 集合类型应用场景
# 去重
l = [1,2,2,2,3,4,4]
print(list(set(l)))















