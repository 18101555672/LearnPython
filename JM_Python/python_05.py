# 模块
# 模块引入
import sys
print('The command line arguments are:')
for i in sys.argv:
    print(i)
print('\n\nThe PYTHONPATH is',sys.path,'\n')

from math import sqrt
print('Square root of 16 is',sqrt(16))

# 模块的 __name__
if __name__=='__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')

# 编写模块
def say_hi():
    print('Hi,this is my module speaking.')
__version__ = '0.1'

# dir函数
# 给出 sys 模块中的属性名称
print(dir(sys))
# 给出当前模块的属性名称
print(dir())
a = 5
print(dir())
