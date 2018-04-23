# 序列类型及操作
l = [1,2,3]
ls = l
list = l.copy()
ls.remove(1)
print(l)
print(ls)
print(list)

lt = []
print(lt)
lt += [1,2,3,4,5]
print(lt)
lt[1] = 'a'
print(lt)
lt.insert(1,'b')
print(lt)
del lt[0]
print(lt)
del lt[0:3]
print(lt)
print(0 in lt)
lt.append(0)
print(lt)
print(lt.index(0))
print(len(lt))
print(max(lt))
print(min(lt))
lt.clear()
print(lt)
