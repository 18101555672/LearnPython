# 更多
# 传递元祖
# 你可曾希望从一个函数中返回两个不同的值？你能做到的。只需要使用一个元组。
def get_error_details():
    return (2,'details')
errnum,errstr = get_error_details()
print(errnum)
print(errstr)
# 在 Python 中交换两个变量的最快方法
a = 5
b = 8
print(a,b)
a,b = b,a
print(a,b)

# 单语句块
if 1 == 1:print('Yes')

# Lambda表格
points = [{'x':2,'y':3},
          {'x':4,'y':1}]
points.sort(key=lambda i:i['y'])
print(points)

# 列表推导
listone = [2,3,4]
listtwo = [2 * i for i in listone if i > 2]
print(listtwo)

# 在函数中接收元组与字典
def powersum(power,*args):
    total = 0
    for i in args:
        total += pow(i,power)
    return total
print(powersum(2,3,4))
print(powersum(3,2,1,2))

# assertt语句
mylist = ['item']
assert len(mylist) >= 1
mylist.pop()
assert len(mylist) >= 0






