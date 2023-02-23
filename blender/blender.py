# 导入 turtle
import turtle

# 新建 turtle 实例
peggy = turtle.Turtle()

# 画蓝瓜的正方形
peggy.fillcolor('blue')
peggy.begin_fill()
for _ in range(4):
    peggy.forward(50)
    peggy.right(90)
peggy.end_fill()

# 画下半部分的小矩形
peggy.fillcolor('white')
peggy.begin_fill()
for _ in range(2):
    peggy.forward(50)
    peggy.right(90)
    peggy.forward(20)
    peggy.right(90)
peggy.end_fill()

# 画左边弧线
peggy.fillcolor('white')
peggy.begin_fill()
peggy.circle(-30, 180)
peggy.end_fill()

# 画蓝色多边形
peggy.fillcolor('blue')
peggy.begin_fill()
peggy.forward(25)
peggy.left(60)
for _ in range(6):
    peggy.forward(15)
    peggy.left(60)
peggy.end_fill()

# 画右边弧线
peggy.fillcolor('white')
peggy.begin_fill()
peggy.circle(30, 180)
peggy.end_fill()
