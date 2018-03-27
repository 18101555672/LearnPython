# 运算符与表达式
# 基础的运算符
# + 加 两个对象相加
print(3 + 5)#8
print('a' + 'b')#ab
# - 减 从一个数中减去另一个数，如果第一个操作数不存在，则假定为零
print(- 5.2)#-5.2
print(50 - 24)#26
# * 乘 给出两个数的乘积或返回字符串重复指定次数后的结果
print(2 * 3)#8
print('la' * 3)#lalala
# ** 乘方 返回X的Y次方
print(3 ** 4)#81
# / 除 X除以Y
print(13 / 3)#4.333333333333333...
# // 整除 X除以Y并对结果向下取整至最接近的整数
print(13 // 3)#4
print(-13 // 3)#-5
# % 取模 返回除法运算后的余数
print(13 % 3)#1
print(-25.5 % 2.25)#1.5

# 求值顺序
print('{:-^40}'.format('求值顺序'))
print('''1 (expressions...), [expressions...], {key: value...}, {expressions...}：表示绑定或元组、表示列表、表示字典、表示集合
2 x[index], x[index:index], x(arguments...), x.attribute：下标、切片、调用、属性引用
3 **：求幂
4 +x, -x, ~x：正、负、按位取反
5 *, /, //, %：乘、除、整除、取余
6 +, -：加与减
7 <<, >>：移动
8 &：按位与
9 ^：按位异或
10 |：按位或
11 in, not in, is, is not, <, <=, >, >=, !=, ==：比较，包括成员资格测试（Membership Tests）和身份测试（Identity Tests）
12 not x：布尔“非”
13 and：布尔“与”
14 or：布尔“或”
15 if - else ：条件表达式
16 lambda：Lambda 表达式
----------END----------''')

# 表达式
length = 5
breadth = 2
area = length * breadth
print('Area is',area)
print('Perimeter is',2 *(length + breadth))