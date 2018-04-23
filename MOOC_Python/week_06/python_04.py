# 字典类型及操作
# del d[k] 删除字典d中键k对应的数据值
# k in d 判断键k是否在字典d中，是则返回True，否则返回False
# d.keys() 返回字典d中所有的键
# d.values() 返回字典d中所有的值
# d.items() 返回字典d中所有的键值对
# d.get(k,<default>) 返回键k相对应的值，若k不存在则返回<default>值
# d.pop(k,<default>) 取出键k相对应的值，若k不存在则返回<default>值
# d.popitem() 随机从字典d中取出一个键值对，以元祖形式返回
# d.clear() 删除所有的键值对
# len(d) 返回字典中元素的个数
d = {}
d = dict()
print(d)
d['mid'] = 'faker'
d['ad'] = 'piglet'
print(d)
d['ad'] = 'bang'
print(d)
print('c' in d)
print(len(d))
for k,v in d.items():
    print(k,v)
d.clear()
print(d)