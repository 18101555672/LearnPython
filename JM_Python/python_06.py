# 数据结构
# 列表List
# 创建一个空列表
mylist = []
# 创建一个列表
shoplist = ['apple','mango','carrot','banana']
# 获取列表中的值的个数
print('I have {} items to purchase.'.format(len(shoplist)))
# 遍历列表
print('These items are:',end=' ')
i = 0
for item in shoplist:
    i = i + 1
    if i < len(shoplist):
        print(item,end=',')
    else:
        print(item,end='.')
# 向列表添加值
print('I also have to buy rice.')
shoplist.append('rice')
print('My shopping list is now',shoplist)
# 向列表排序
print('I will sort my list now')
shoplist.sort()
print('Sorted shopping list is',shoplist)
# 向列表删除值
print('The first item i will buy is',shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought the',olditem)
print('My shopping list is now',shoplist)

# 元祖Tuple
zoo = ('python','elephant','penguin')
print('Number of animals in the zoo is',len(zoo))
new_zoo = 'monkey','camel',zoo
print('Number of cages in the new zoo is',len(new_zoo))
print('All animals in new zoo are',new_zoo)
print('Last animal brought from old zoo is',new_zoo[2][2])
print('Number of animals in the new zoo is',len(new_zoo)-1+len(new_zoo[2]))
# 创建一个空的元祖
mytuple = ()
# 创建一个只有一个值的元祖
nulltuple = (2,)

# 字典Dictionary
# 创建一个空字典
myDictionary = {}
# 创建一个字典
ab = {
    'Swaroop':'swaroop@swaroopch.com',
    'Larry':'larry@wall.org',
    'Matsumoto':'matz@ruby-lang.org',
    'Spammer':'spammer@hotmail.com'
}
# 通过键获取值
print('Swaroop\'s address is',ab['Swaroop'])
# 删除一对键值对
del ab['Spammer']
# 获取共有多少对键值对
print('There are {} contacts in the address-book'.format(len(ab)))
# 遍历字典
for name,address in ab.items():
    print('Contact {} at {}'.format(name,address))
# 添加一对键值对
ab['Guido'] = 'guido@python.org'
# 成员资格测试，判断某个键是否在字典中
if 'Guido' in ab:
    print('Guido\'s address is',ab['Guido'])
else:
    print('Guido is not in ab')

# 切片（Slicing）运算符
demo = 'wuchenyang'
# 获取第一位
print(demo[0])
# 获取第六位
print(demo[5])
# 获取倒数第一位
print(demo[-1])
# 获取倒数第四位
print(demo[-4])
# 获取2-3位
print(demo[1:3])
# 获取第三位之后的（包括第三位）
print(demo[2:])
# 获取第二位到倒数第一位（不包括倒数第一位）
print(demo[1:-1])
# 从第二位开始每隔两位获取一个值
print(demo[1::2])

# 集合Set
# 创建一个空集合
myset = set()
# 创建一个集合
bri = set(['brazil','russia','india'])
# 成员资格测试
print('india' in bri)
print('usa' in bri)
# 复制一个集合
bric = bri.copy()
# 向集合中添加值
bric.add('china')
print(bric)
# 向集合中删除值
bri.remove('russia')
print(bri)
# 集合运算
x = {1,2,3,4}
y = {3,4,5,6}
# 交集
print(x & y)
print(x.intersection(y))
# 并集
print(x | y)
print(x.union(y))
# 差集
print(x - y)
print(x.difference(y))
print(y - x)
print(y.difference(x))
# 对称差集
print(x ^ y)
print(x.symmetric_difference(y))
# 集合的子集和超集
z = {1,2,3}
print(z.issubset(x))
print(z.issubset(y))
print(x.issuperset(z))
print(y.issuperset(z))

# 有关字符串的更多内容
name = 'Swaroop'
# startswith方法查询字符串是否以给定的字符串开头
if name.startswith('Swa'):
    print('Yes, the string starts with "Swa"')
# in运算符用以查询字符串中是否包含所给定的字符串
if 'a' in name:
    print('Yes, it contains the string "a"')
# find方法用于定位字符串中给定的子字符串的位置，如果找不到相应的子字符串，则返回-1.
if name.find('war') != -1:
    print('Yes, it contains the string "war"')
# join方法用于将所给定的字符串作为每一项目之间的分隔符
l = ['Brazil', 'Russia', 'India', 'China']
print('_*_'.join(l))