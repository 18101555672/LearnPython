# 函数的定义与使用
def func():
    return 1,2,3
f = func()
print(f)
a,b,c = func()
print(a)
print(b)
print(c)

# lambda 函数（谨慎使用）
f = lambda x,y:x+y
print(f(10,15))
f = lambda :'lambda函数'
print(f())