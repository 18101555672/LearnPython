# 代码复用与函数递归
# 计算 n! 阶乘
# 使用递归
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact( n - 1 )
print(fact(10))
# 不使用递归
def getFact(n):
    s = 1
    if n == 0:
        return 1
    else:
        for i in range( 1, n + 1):
            s = s * i
        return s
print(getFact(10))

# 递归实例解析
# 字符串反转
s = 'Hello World'
print(s[::-1])
def rvs(s):
    if s == '':
        return ''
    else:
        return rvs(s[1:]) + s[0]
print(rvs('abcd'))

# 斐波那契数列
# F(n) = F(n-1) + F(n-2)
def FBNQ(n):
    if n == 1 or n == 2:
        return 1
    else:
        return FBNQ(n - 1) + FBNQ(n - 2)
print(FBNQ(10))

# 汉诺塔数列
count = 0
def hanoi(n,src,dst,mid):
    global count
    if n == 1:
        print('{}:{}->{}'.format(1, src, dst))
        count += 1
    else:
        hanoi(n - 1, src, mid, dst)
        print('{}:{}->{}'.format(n, src, dst))
        count += 1
        hanoi(n - 1, mid, dst, src)
hanoi(3,'A','B','C')
print(count)









