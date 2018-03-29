# encoding=utf-8
# 输入与输出
# 通过help(str)了解更多关于str函数的细节
print(help(str))
a = 'wcy'
# rjust方法可以获得一个右对齐到指定宽度的字符串
print(a.rjust(10))

# 用户输入内容
def reverse(text):
    # 切片的第三个参数为-1，将返回翻转过的文本
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

something = input('Enter text:')
if is_palindrome(something):
    print('Yes, it is a palindrome')
else:
    print('No, it is not a palindrome')

# 作业练习
# 检查文本是否属于回文
t = input('Enter:')
forbidden = (' ',',','.','!','?')
tt = []
for i in t:
    if i not in forbidden:
        # str.upper()小写转大写，str.lower()大写转小写
        tt.append(str.lower(i))
if tt == tt[::-1]:
    print('Yes, it is a palindrome')
else:
    print('No, it is not a palindrome')

# 文件
poem = '''\
Programming is fun
when the work is done
if you wanna make your work also fun:
    use Python!
'''
# 打开文件以编辑（ 'w'riting 写入模式）
# 如果没有特别指定，默认启用 'r'ead 阅读模式
# encoding参数指定编码格式
f = open('poem.txt','w',encoding='utf-8')
# 向文件中编写文本
f.write(poem)
# 关闭文件
f.close()
f = open('poem.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line,end='')
f.close()
# 常用的模式：阅读模式（r），写入模式（w），追加模式（a），文本模式（t），二进制模式（b）

# Pickle
# Python 提供了一个叫作 Pickle 的标准模块，通过它你可以将任何纯 Python 对象存储到一个文件中，并在稍后将其取回。这叫作持久地（Persistently）存储对象。
import pickle
# 我们存储相关对象的文件的名称
shoplistfile = 'shoplist.data'
# 需要购买的物品清单
shoplist = ['apple','mango','carrot']
# 准备写入文件
f = open(shoplistfile,'wb')
# 转储对象至文件
pickle.dump(shoplist,f)
# 关闭文件
f.close()
# 清除 shoplist 变量
del shoplist
# 重新打开存储文件
f = open(shoplistfile,'rb')
# 从文件中载入对象
storedlist = pickle.load(f)
print(storedlist)


