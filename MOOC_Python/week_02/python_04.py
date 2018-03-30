# 基本图形绘制练习
import turtle
# 绘制正方形
turtle.setup(800, 800)
turtle.pensize(5)
def DrawSquare():
    turtle.fd(100)
    for i in range(3):
        turtle.left(90)
        turtle.fd(100)

# 绘制六边形
def DrawHexagons():
    turtle.fd(100)
    for i in range(5):
        turtle.left(60)
        turtle.fd(100)

# 绘制叠边形
def DrawEdgeShape():
    turtle.fd(100)
    for i in range(8):
        turtle.left(80)
        turtle.fd(100)

# 绘制同切圆
def DrawSameTangentCircle():
    for i in range(4):
        turtle.circle((i+1)*20+30)

if __name__=='__main__':
    # DrawSquare()
    # DrawHexagons()
    # DrawEdgeShape()
    DrawSameTangentCircle()
turtle.done()


