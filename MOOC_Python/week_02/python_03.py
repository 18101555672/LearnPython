# turtle程序语法元素分析
import turtle

# 画笔控制函数
# 抬起画笔，海龟不再有行进轨迹
# turtle.penup() / turtle.pu
# 落下画笔，海龟有行进轨迹
# turtle.pendown() / turtle.pd()
# 设置画笔宽度
# turtle.pensize(width) / turtle.width(width)
# 设置画笔颜色
# color为颜色字符串或RGB值
# turtle.pencolor(color)
# 颜色字符串
turtle.pencolor('purple')
# RGB小数值
turtle.pencolor(0.63,0.13,0.94)
# RGB元组值
turtle.pencolor((0.63,0.13,0.94))

# 运动控制函数
# 向前直线行进
# d为负数则倒退行进
# turtle.forward(d) / turtle.fd(d)
# 根据半径r绘制extent角度的弧形
# r：默认圆心在海龟左侧r举例的位置
# extent：绘制角度，默认是360度整圆
# turtle.circle(r,extent=None)
turtle.circle(100)
turtle.circle(-100,90)

# 方向控制函数
# 只改变海龟的行进方向，不进行行进
# 改变行进方向，海龟走角度
# angle：将海龟的方向转换成给定的绝对角度
# turtle.setheading(angle) / turtle.seth(angle)
# 向左改变方向
# turtle.left(angle)
# 向右改变方向
# turtle.right(angle)

# 添加done()绘制完成后不会自动退出，不添加则绘制完成后自动退出
# turtle.done()

