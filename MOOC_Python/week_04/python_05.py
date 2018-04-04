# 实例：圆周率的计算
# 蒙特卡罗方法
import random,time
DARTS = 1000*100000
hits = 0.0
start = time.perf_counter()
for i in range(1,DARTS+1):
    x,y = random.random(),random.random()
    dist = pow(x ** 2 + y ** 2, 0.5)
    if dist <= 1.0:
        hits += 1
    pi = 4 * (hits/DARTS)
print(pi)
print(time.perf_counter()-start)