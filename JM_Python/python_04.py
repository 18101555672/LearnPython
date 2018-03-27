# 函数
def say_hello():
    print('hello world')
say_hello()
say_hello()

# 函数参数
# 在定义函数时所给定的参数名称称作‘形参’（Parameters）
# 在调用函数时所提供给函数的值称作‘实参’（Arguments）
def print_max(a,b):
    if a > b:
        print('{} is maximum'.format(a))
    elif a < b:
        print('{} is maximum'.format(b))
    else:print('{} is equal to {}'.format(a,b))
x = 6
y = x
print_max(7,8)
print_max(x,y)

# 局部变量
a = 50
def func(a):
    print('a is {}',a)
    a = 2
    print('Changed local a to',a)
func(a)
print('a is still',a)

# global语句
b = 50
def funcc():
    global b
    print('b is',b)
    b = 2
    print('Changed global b to',b)
funcc()
print('Value of b is',b)

# 默认参数值
def say(message,time=1):
    print(message * time)
say('Hello')
say('Hi',3)

# 关键字参数
def keyWord(a,b=5,c=10):
    print('a is {} and b is {} and c is {}'.format(a,b,c))
keyWord(3,7)
keyWord(25,c = 24)
keyWord(c = 50,a = 100)

# 可变参数
def total(a=5,*numbers,**phonebook):
    print('a:',a)
    for single_item in numbers:
        print('single_item:',single_item)
    for first_part,second_part in phonebook.items():
        print(first_part,':',second_part)
total(10,1,2,3,Jack=1123,John=2231,Inge=1560)

# return语句
def maximum(x,y):
    if x > y:
        return x
    elif x == y:
        return 'The numbers are equal'
    else:
        return y
print(maximum(2,3))
print(maximum(3,3))

def nothing():
    pass
print(nothing())

# 文档字符串DocStrings
def print_min(x,y):
    '''打印两个数值中的最大数。

    这两个数都应该是整数'''
    x = int(x)
    y = int(y)
    if x > y:
        print(y,'is minimum')
    elif x < y:
        print(x,'is minimum')
    else:
        print('They are equal')
print_min(3,5)
print_min(6,6)
print(print_min.__doc__)
