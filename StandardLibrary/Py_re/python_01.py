# 正则表达式
import re
# re.match(pattern, string, flags=0)
# 尝试从字符串的起始位置匹配一个表达式，成功匹配则返回匹配的对象，否则返回None
# 只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败
# pattern 匹配的正则表达式
# string 要匹配的字符串
# flags 标志位，用于控制正则表达式的匹配方式
print(re.match('A','abc'))
print(re.match('A','Abc'))
print(re.match('A','Abc').span())
print(re.match('A','aAc'))

# match和search的区别
# re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None
# re.search匹配整个字符串，直到找到一个匹配
line = 'Cats are smarter than dogs'
m = re.match(r'dogs',line,re.M|re.I)
if m:
    print('match --> m.group():',m.group())
else:
    print('No match!')
m = re.search(r'dogs',line,re.M|re.I)
if m:
    print('search --> m.group():',m.group())
else:
    print('No match')

# 匹配对象方法
# group(num=0) 匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
# groups() 返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。
matchObj = re.match(r'(.*) are (.*?) .*',line,re.M|re.I)
if matchObj:
    print('matchObj.group():',matchObj.group())
    print('matchObj.group(0):',matchObj.group(0))
    print('matchObj.group(1):',matchObj.group(1))
    print('matchObj.group(2):',matchObj.group(2))
    print('matchObj.groups():',matchObj.groups())
else:
    print('No match!')

# 检索和替换
# re.sub(pattern,repl,string,count=0)
# pattern 正则中的模式字符串
# repl 替换的字符串，也可以为一个函数
# string 要被查找替换的原始字符串
# count 模式匹配后替换的最大次数，默认0表示替换所有的匹配
phone = '2004-959-559 # 这是一个电话号码'
num = re.sub(r'#.*$','',phone)
print(num)
num = re.sub(r'\D','',phone)
print(num)

def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)
s = 'A23G4HFG567'
print(re.sub('(?P<value>\d+)',double,s))

# compile函数用于编译正则表达式，生辰一个正则表达式对象
# re.compile(pattern[,flags])
# pattern 一个字符串形式的正则表达式
# flags 表示匹配模式，可选
s = 'one12twothree34four'
pattern = re.compile(r'\d+')
m = pattern.match(s)
print(m)
m = pattern.match(s,2,10)
print(m)
m = pattern.match(s,3,10)
print(m)
print(m.group())
# 用于获取分组匹配的子串在整个字符串中的起始位置（子串第一个字符的索引），参数默认值为 0
print(m.start())
# 用于获取分组匹配的子串在整个字符串中的结束位置（子串最后一个字符的索引+1），参数默认值为 0
print(m.end())
# 返回 (start(group), end(group))
print(m.span())

# findall函数在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表
# 注意： match 和 search 是匹配一次 而 findall 是匹配所有
# findall(string[,pos[,endpos]])
# string 待匹配的字符串
# pos 可选参数，指定字符串的其实位置，默认为0
# endpos 可选参数，指定字符串的结束位置，默认为字符串的长度
pattern = re.compile(r'\d+')
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('runoob123google456')
result21 = pattern.findall('runoob123google456',0,10)
result3 = pattern.findall('dashdkhasjkd')
print(result1)
print(result2)
print(result21)
print(result3)

# finditer函数在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回
result4 = pattern.finditer('1a2b3c')
print(result4)
for i in result4:
    print(i)
    print(i.group())

# split方法按照能够匹配的子串将字符串分割后返回列表
# re.split(pattern,string[,maxsplit=0,flags=0])
# pattern 匹配的正则表达式
# string 要匹配的字符串
# maxsplit 分割次数，默认为0不限次
# flags 标志位
print(re.split(',','runoob1,runoob2,runoob.'))
print(re.split(',','runoob1,runoob2,runoob.',1))

# 正则表达式修饰符
# 可选标志
# re.I 使匹配对大小写不敏感
# re.L 做本地化识别匹配
# re.M 多行匹配，影响 ^ 和 &
# re.S 使 . 匹配包括换行在内的所有字符
# re.U 根据Unicode字符集解析字符，这个标志影响\w,\W,\b,\B
# re.X 该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解

# 正则表达式模式
# ^ 匹配字符串的开头
# $ 匹配字符串的末尾
# . 匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符
# [...] 用来表示一组字符，单独列出：[amk]匹配'a','m'或'k'
# [^...] 不在[]中的字符：[^abc]匹配除了a,b,c之外的字符
# * 匹配任意个
# + 至少匹配一个
# ? 匹配0个或1个，非贪婪方式
# {n} 匹配n个
# {n,} 匹配n个或者n个以上
# {n,m} 匹配n到m个，贪婪方式
# a|b 匹配a或b
# ( ) G匹配括号内的表达式，表示一个组
# \w 匹配数字字母下划线
# \W 匹配非数字字母下划线
# \s 匹配任意空白字符
# \S 匹配任意非空白字符
# \d 匹配任意数字,等价于[0-9]
# \D 匹配任意非数字
# \A 匹配字符串开始
# \Z 匹配字符串结束，如果存在换行，只匹配到换行前的结束字符串
# \z 匹配字符串结束
# \G 匹配最后匹配完成的位置
# \b 匹配一个单词边界，也就是指单词和空格间的位置：例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'
# \B 匹配非单词边界：例如，'er\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er
# \n,\t等 匹配一个换行符，制表符等
# 实例：
# [Pp]ython 匹配'Python'或'python'
# [abc] 匹配'a'或者'b'或者'c'
# [^abc] 匹配除'a'或者'b'或者'c'以外的
# [0-9] 匹配任何数字，类似[012345679]或\d
# [^0-9] 匹配除数字以外的
# [a-z] 匹配任何小写字母
# [A-Z] 匹配任何大写字母
# [a-zA-Z]匹配任何字母
# [a-zA-Z0-9]匹配任何字母和数字

# 练习1：验证出类似的Email
mail1 = 'someone@gmail.com'
mail2 = 'bill.gates@microsoft.com'
r = re.compile(r'([\w]+|[\w]+.[\w]+)@([a-zA-Z0-9]+).([a-zA-Z0-9]{2,})')
print(r.match(mail1))
print(r.match(mail1).group())
print(r.match(mail1).group(1))
print(r.match(mail1).group(2))
print(r.match(mail1).group(3))
print(r.match(mail1).groups())
print(r.match(mail2))
print(r.match(mail2).group())
print(r.match(mail2).group(1))
print(r.match(mail2).group(2))
print(r.match(mail2).group(3))
print(r.match(mail2).groups())
# 练习2：验证并提取出带名字的Email地址
mail3 = '<Tom Paris> tom@voyager.org'
r = re.compile(r'<(.*)> ([\w]+|[\w]+.[\w]+)@([a-zA-Z0-9]+).([a-zA-Z0-9]{2,})')
print(r.match(mail3))
print(r.match(mail3).group())
print(r.match(mail3).group(1))
print(r.match(mail3).groups())
















