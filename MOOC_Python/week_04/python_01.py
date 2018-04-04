# encoding=utf-8
# 程序的分支结构

# 单分支结构
if True:
    print('True')

# 二分支结构
guess = 99
if guess == 99:
    print('yes')
else:
    print('no')
# 紧凑形式 <表达式1> if 条件 else <表达式2>
print('yes' if guess == 99 else 'no')

# 多分支结构
score = 55
if score == 100:
    print('S')
elif score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('不及格')

# 条件组合
# and 两个条件x和y的逻辑与
# or  两个条件x和y的逻辑或
# not 条件x的逻辑非
# if guess != 99:（同下）
if guess > 99 or guess < 99:
    print('no')
else:
    print('yes')

# 异常处理
# 尝试执行try下的程序
try:
    num = eval(input('Enter a number:'))
# 如果报错，则执行except下的语句
except:
    print('not a number!')
# 如果没有报错，则执行else下的语句
else:
    print(num ** 2)
# 不管怎样最终都会执行finally下的语句
finally:
    print('Done')
























