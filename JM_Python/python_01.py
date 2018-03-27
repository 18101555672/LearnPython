print('hello world')
# 基础
# 更详细的格式化方法
print('{:-^40}'.format('更详细的格式化方法'))
# 对于浮点数‘0.333’保留小数点后三位
print('{:.3f}'.format(1.0/3))
# 使用指定符号填充文本，并保持文字处于中间位置
print('{:^11}'.format('hello'))
print('{:_^11}'.format('hello'))
print('{:0^11}'.format('hello'))
# 基于关键词输出
print('{name} wrote {book}'.format(name='Swaroop',book='A Byte of Python'))

# 使用end指定print函数以什么结尾（默认为 \n 换行符）
print('{:-^40}'.format('使用end指定print函数的结尾'))
print('a',end='')
print('b')
print('a',end='|')
print('b',end='|')
print('c')

# 转义序列
print('{:-^40}'.format('转义序列'))
print('This is the first line\nThis is the second line')
print('This is the first sentence.\
This is the second sentence.')

# 原始字符串
print('{:-^40}'.format('原始字符串'))
print(R'Newlines are indicated by \n')
print(r'Newlines are indicated by \n')

# 变量命名规则（标识符）
print('{:-^40}'.format('变量命名规则（标识符）'))
print('''1.第一个字符必须是字母表中的字母（大写ASCII字符或小写ASCII字符或者Unicode字符）或下划线
2.标识符的其他部分可以由字符（大写ASCII字符或小写ASCII字符或者Unicode字符）、下划线（_）、数字（0-9）组成
3.标识符名称区分大小写''')

