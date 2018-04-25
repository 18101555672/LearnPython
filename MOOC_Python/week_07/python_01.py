# encoding=utf-8
# 文件的使用
# 用文本模式读取
tf = open('f.txt','rt')
print(tf.read())
tf.close()
# 用二进制模式读取
bf = open('f.txt','rb')
print(bf.read())
bf.close()

# 打开模式
# 'r' 只读模式，默认值，如果文件不存在，返回FileNotFoundError
# 'w' 覆盖写模式，文件不存在则创建，存在则覆盖
# 'x' 创建写模式，文件不存在则创建，存在则返回FileExistsError
# 'a' 追加写模式，文件不存在则创建，存在则在文件最后追加内容
# 'b' 二进制文件模式
# 't' 文本文件模式，默认值
# '+' 与r,w,x,a一同使用，在原功能基础上增加同时读写功能

# 操作方法
# f.read(size=-1) 读入全部内容，如果给出参数size，读入前size长度
# f.readline(size=-1) 读入一行内容，如果给出参数size，读入该行前size长度
# f.readlines(hint=-1) 读入文件所有行，以每行为元素形成列表，如果给出参数hint，读入前hint行

# 数据文件写入
# f.write(s) 想文件写入一个字符串或字节流s
# f.writelines(lines) 将一个元素全为字符串的列表写入文件
# f.seek(offset) 改变当前文件操作指针的位置：0 文件开头；1 当前位置；2 文件结尾

fo = open('output.txt','w+')
ls = ['中国','法国','美国']
fo.writelines(ls)
fo.seek(0)
for line in fo:
    print(line)
fo.close()












