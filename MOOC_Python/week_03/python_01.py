# encoding=utf-8
# 数字类型及操作
# 四种进制表示形式
# 十进制：1010、99、-217
# 二进制，以0b或0B开头：0b010、-0B101
# 八进制，以0o或0O开头：0o123、-0O456
# 十六进制，以0x或0X开头：0x9a、-0X89

# 浮点数
# 取值范围和精度基本无限制
# 运算存在不确定位数，所以进行浮点数比较时要使用round函数
# 四舍五入函数round()
# x为要四舍五入的数值，d为小数截取位数，d默认为0
# round(x,d)
print(round(3.1415456,1))
print(round(3.1415456,3))
print(round(3.1415456,5))

# 科学计数法
# 使用e或E作为幂的符号 ，以10为基数，格式如下：
# <a>e<b> 表示a*10^b（a乘10的b次方）
# 例1：4.3e-3 值为 0.0043（4.3*10^-3）
# 例2：9.6E5  值为960000 （9.6*10^5）

# 复数
# a + bj 被称为复数，a是实部，b是虚部
z = 1.23e-4 + 5.6e+89j
# 获取实部
print(z.real)
# 获取虚部
print(z.imag)

# 素质运算函数
# 计算绝对值abs(x)，输出x的绝对值
print(abs(-10))
# 计算商余divmod(x,y)，同时输出商和余数
print(divmod(10,4))
# 计算幂余pow(x,y,z)，输出x**y，z表示显示后几位
print(pow(3,99))
print(pow(3,99,1000))
# 输出最大值
print(max(1,2,3))
# 输出最小值
print(min(1,2,3))
# int函数，转换成整数
# 不进行四舍五入运算
print(int(123.45))
print(int(123.54))
print(int('123'))
# float函数，转换成浮点数
print(float(12))
print(float('1.23'))
print(float('1'))
# complex函数，转换成复数
print(complex(4))
print(complex(4.1))