# PyInstaller库的使用
# 常用参数
# -h 查看帮助
# --clean 清理打包过程中的临时文件
# -D,--onedor 默认值，生成dist文件夹
# -F,--onefile 在dist文件夹中只生成独立的打包文件
# -i<图标文件名.ico> 指定打包程序使用的图标文件
# 只有的打包过程中需要用到PyInstaller库
# 打包完成后在别的平台上可以直接打开，不需要用到PyInstaller库
# PyInstaller -i icoName.ico -F PyFileName.py