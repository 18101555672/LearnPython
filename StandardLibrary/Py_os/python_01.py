import os
# 文件/目录方法
# os.chdir(path) 改变当前工作目录：path 要切换到的新路径
# os.getcwd() 返回当前工作目录
print(os.getcwd())
os.chdir('D:\LearnPython')
print(os.getcwd())
os.chdir('D:\LearnPython\StandardLibrary\Py_os')

# os.listdir(path) 获取指定文件夹中所有内容的名称列表：path 要获取的路径，默认为当前工作目录
print(os.listdir())
print(os.listdir('D:\LearnPython'))

# os.mkdir(path,mode=0o777) 创建文件夹：path 要创建的文件夹的路径 mode 设置目录的权限数字模式，默认为0o777（八进制）
os.mkdir('osmkdir')

# os.makedirs(path,mode=0o777) 递归创建文件夹
os.makedirs('makedirs/a/b/c')

# os.rmdir(path) 删除空目录，目录必须是空，否则抛出OSError：path 要删除的目录路径
os.rmdir('osmkdir')

# os.removedirs(path) 递归删除目录，必须都是空目录
os.removedirs('makedirs/a/b/c')

# os.rename(src,dst) 要修改的文件或目录名，修改后的名称
os.rename('foo.txt','foo0.txt')
os.rename('foo0.txt','foo.txt')

# os.stat(path) 获取文件或目录的信息
# st_mode: inode 保护模式
# st_ino: inode 节点号。
# st_dev: inode 驻留的设备。
# st_nlink: inode 的链接数。
# st_uid: 所有者的用户ID。
# st_gid: 所有者的组ID。
# st_size: 普通文件以字节为单位的大小；包含等待某些特殊文件的数据。
# st_atime: 上次访问的时间。
# st_mtime: 最后一次修改的时间。
# st_ctime: 由操作系统报告的"ctime"。在某些系统上（如Unix）是最新的元数据更改的时间，在其它系统上（如Windows）是创建时间（详细信息参见平台的文档）。
print(os.stat('foo.txt'))

# 环境变量
# os.getenv(key) 获取系统环境变量
print(os.getenv('PATH'))

# os.putenv(key,path) 将一个目录添加到环境变量中（临时增加仅对当前脚本有效）
# os.putenv('PATH','a/b/c')

# 常用值
# os.curdir 表示当前文件夹：返回 . 可忽略
print(os.curdir)

# os.pardir 表示上层文件夹：返回 .. 不可忽略
print(os.pardir)

#os.mkdir('../../../man') 相对路径 从当前目录开始查找
#os.mkdir('/home/sy/man1') 绝对路径 从根目录开始查找

# os.name 获取代表操作系统的名称字符串 linux & unix -> posix ; window -> nt
print(os.name)

# os.sep 获取系统路径间隔符号 linux -> / ; window -> \
print(os.sep)

# os.extsep 获取文件名称和后缀之间的间隔符号 window & linux -> .
print(os.extsep)

# os.linesep 获取操作系统的换行符号 window -> \r\n ; linux & unix -> \n
print(os.linesep)

# os.path子模块
# os.path.abspath(path) 将相对路径转换为绝对路径
path = './boys'
print(os.path.abspath(path))

# os.path.dirname(path) 获取完整路径当中的目录部分
print(os.path.dirname(os.getcwd()))

# os.path.basename(path) 获取完整路径当中的主体部分
print(os.path.basename(os.getcwd()))

# os.path.split(path) 将一个完整的路径切割成目录部分和主体部分
print(os.path.split(os.getcwd()))

# os.path.splitext(path) 将一个路径切割成文件后缀和其他两个部分，主要用于获取文件的后缀
print(os.path.splitext('D:\LearnPython\StandardLibrary\Py_os\python_01.py'))

# os.path.join(path1,path2) 将两个路径合并成一个
print(os.path.join(os.getcwd(),'join.txt'))

# os.path.getsize(path) 获取文件大小（字节）
print(os.path.getsize(os.getcwd()))

# os.path.isfile(path) 检测是否是文件
print(os.path.isfile('D:\LearnPython\StandardLibrary\Py_os\python_01.py'))
print(os.path.isfile('D:\LearnPython\StandardLibrary\Py_os'))

# os.path.isdir(path) 检测是否是目录
print(os.path.isdir('D:\LearnPython\StandardLibrary\Py_os\python_01.py'))
print(os.path.isdir('D:\LearnPython\StandardLibrary\Py_os'))

import time
# os.path.getctime(path) 获取文件的创建时间
print(time.ctime(os.path.getctime(os.getcwd())))
# os.path.getmtime(path) 获取文件的修改时间
print(time.ctime(os.path.getmtime(os.getcwd())))
# os.path.getatime(path) 获取文件的访问时间
print(time.ctime(os.path.getatime(os.getcwd())))

# os.path.exists(path) 检测路径是否存在
print(os.path.exists('D:\LearnPython\StandardLibrary\Py_os'))
print(os.path.exists('D:\LearnPython\StandardLibrary\Py_os\exists'))

# os.path.isabs(path) 检测是否是绝对路径
print(os.path.isabs('D:\LearnPython\StandardLibrary\Py_os'))
print(os.path.isabs('..\Py_os'))