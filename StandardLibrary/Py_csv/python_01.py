import csv
# 读取文件
# 方法一：使用reader函数
with open('csvFile.csv','r',encoding='utf-8') as f:
    reader = csv.reader(f)
    rows = [row for row in reader]
print(rows)
# 读取其中某一列
with open('csvFile.csv','r',encoding='utf-8') as f:
    reader = csv.reader(f)
    column = [row[1] for row in reader]
print(column)
# 方法二：使用DictReader
with open('csvFile.csv','r',encoding='utf-8') as f:
    reader = csv.DictReader(f)
    column = [row for row in reader]
print(column)
# 读取其中某一列
with open('csvFile.csv','r',encoding='utf-8') as f:
    reader = csv.DictReader(f)
    column = [row['A'] for row in reader]
print(column)

# 写文件
with open('csvFile.csv','a',encoding='utf-8',newline='') as f:
    row = ['一','二','三','四']
    f = csv.writer(f)
    f.writerow(row)
