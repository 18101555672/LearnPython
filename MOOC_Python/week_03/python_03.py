# 实例：文本进度条
import time
print('{:-^20}'.format('执行开始'))
print('执行开始'.center(20,'-'))
scale = 50
start = time.perf_counter()
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i / scale) * 100
    dur = time.perf_counter() - start
    # \r 将光标定位在行首
    print('\r{:^3}%[{}->{}]{:0.2f}s'.format(c,a,b,dur),end='')
    time.sleep(0.1)
print('\n{:-^20}'.format('执行结束'))