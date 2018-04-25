# 数据的格式化和处理
# CSV Comma-Separated Values
# 国际通用的一二维数据存储格式，一般为 .csv 扩展名
# 每行一个一维数据，采用逗号分隔，没有空行
# Excel可以读入输出，一般的编辑软件都可以产生
# 如果某个元素缺失，逗号仍要保留
# 二维数据的表头可以作为数据存储，也可以另行存储
# 逗号为英文半角逗号，逗号与数据之间无额外空格
# 二维数据一般索引习惯，先行后列：ls[row][column]

ls = [[123],[456],[789]]
with open('csvFile.csv','w') as f:
    for i in ls:
        t = str(i).replace('[','')
        t = t.replace(']','')
        f.write(','.join(t) + '\n')
