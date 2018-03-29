# 异常
# NameError 名称错误
# EOFError（End of File Error）文件结尾错误

# 处理异常
try:
    text = input('Enter something -->')
except EOFError:
    print('Why did you do an EOF on me?')
except KeyboardInterrupt:
    print('You cancelled the operation.')
else:
    print('You enered {}'.format(text))
finally:
    print('Done')

# 抛出异常
class ShortInputException(Exception):
    '''一个由用户定义的异常类'''
    def __init__(self,length,atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast
try:
    text = input('Enter something:')
    if len(text) < 3:
        raise ShortInputException(len(text),3)
except EOFError:
    print('Why dir you do an EOF on me?')
except ShortInputException as ex:
    print(('ShortInputException:The input was' + ' {} long, expection at least {}').format(ex.length,ex.atleast))
else:
    print('No exception was raised.')

# Try...Finally
import sys,time
f = None
try:
    f = open('poem.txt')
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line,end='')
        # sys.stdout.flush()能将结果立即打印到屏幕上。
        sys.stdout.flush()
        print('Press ctrl + c now')
        time.sleep(2)
except IOError:
    print('Could not find file poem.txt')
except KeyboardInterrupt:
    print('!! You cancelled the reading from the file.')
finally:
    if f:
        f.close()
    print('(Cleaning up: Closed the file)')

# witht语句
with open('poem.txt') as f:
    for line in f:
        print(line,end='')




