# encoding=utf-8
# turtle库的使用
import turtle

# turtle绘图窗体布局
# setup()设置窗体大小及位置
# 前两个参数表示窗体大小
# 后两个参数表示窗体位置（以屏幕左上角为原点(0,0)）
# 后两个是可选参数,不填表示在屏幕正中间
# setup()不是必须的
# turtle.setup(width,height,startx,starty)

# turtle空间坐标体系
# goto()让任何位置的海龟去到达某个位置
# turtle.goto(x,y)
# 向海龟的正前面行进
# turtle.fd(d)
# 向海龟的反方向行进
# turtle.bk(d)
# circle()以海龟当前位置左侧的某一个点为圆心进行曲线行进
# turtle.circle(r,angle)

# turtle角度坐标体系
# seth()改变海龟行进方向
# 只改变方向不行进
# angle为绝对度数
# turtle.seth(angle)
# 向左改变方向
# turtle.left(angle)
# 向右改变方向
# turtle.right(angle)


# RGB色彩体系
# turtle.colormode(mode)
# 默认采用小数值，可切换为整数值
# 1.0：RGB小数值模式
# 255：RGB整数值模式