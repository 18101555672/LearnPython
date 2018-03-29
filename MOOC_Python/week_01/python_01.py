# 实例1：温度转换
def temperatureChang(value,unit='F'):
    if unit == 'F':
        return '{}℃ ==> {:.2f}℉'.format(value,value*9/5+32)
    elif unit == 'C':
        return '{}℉ ==> {:.2f}℃'.format(value,5/9*(value-32))
    else:
        return 'The second parameter please enter F or C'
print(temperatureChang(18,'F'))
print(temperatureChang(84,'C'))
print(temperatureChang(55,'A'))

TempStr = input('请输入带有符号的温度值：')
if TempStr[-1] in ['F','f']:
    # eval() 去掉参数最外侧引号并执行余下语句
    C = (eval(TempStr[0:-1]) - 32) / 1.8
    print('转换后的温度是{:.2f}℃'.format(C))
elif TempStr[-1] in ['C','c']:
    F = 1.8*eval(TempStr[0:-1]) + 32
    print('转换后的温度是{:.2f}℉'.format(F))
else:
    print('输入格式错误')

