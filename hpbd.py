import time
import turtle
import tkinter.messagebox as mb
import tkinter as tk
import webbrowser

# 输入姓名和生日
name = input("请输入您的姓名:")
birthyear = int(input("请输入您的出生年份："))
birthday = input("请输入您的生日(格式为:月/日):")

# 获取当前时间
current_time = time.strftime("%m/%d")
current_year = int(time.strftime("%Y"))

# 计算年龄
age = current_year - birthyear


# 判断今天是否是您的生日
if current_time == birthday:
    message = "再次祝{}{}岁生日快乐！\(^w^)/".format(name, age)
    mb.showinfo("提示", "送您个惊喜 ( •̀ ω •́ )y")
       # 创建Turtle窗口
    window = turtle.Screen()     #17.5cm —— * 14.5cm | / fd42 = 1cm
                                 # cake= 12.5cm —— * 9.5cm | / goto +100 = +2.5cm
    # 画蛋糕🎂
    def draw_cake():
      window.title("🎂HpBd🎂")     # turtle 窗口标题
      window.bgcolor("pink")      #turtle 背景颜色
      turtle.speed(0)             #笔迹行走速度
      turtle.penup()              #取消作画（不取消会连着笔迹一起定位）
      turtle.goto(-262.5, -199.5) #定位
      turtle.pendown()            #开始作画
      turtle.color('red')         #笔迹颜色
      turtle.forward(516.6)       #第一层蛋糕框
      turtle.left(90)
      turtle.forward(122)
      turtle.left(90)
      turtle.forward(516.6)
      turtle.left(90)
      turtle.forward(123)
      turtle.circle(64.5, -180)   #馅料
      turtle.circle(-64.5, 180)
      turtle.circle(64.5, -180)
      turtle.circle(-64.5, 180)
      turtle.right(90)
      turtle.forward(31.9)        #内馅
      turtle.right(90)
      turtle.circle(31.75, 180)  
      turtle.right(90)
      turtle.forward(66)
      turtle.right(90)
      turtle.circle(31.75, 180)
      turtle.right(90)
      turtle.forward(66)
      turtle.right(90)
      turtle.circle(31.75, 180)
      turtle.right(90)
      turtle.forward(66)
      turtle.right(90)
      turtle.circle(31.75, 180)
      turtle.penup()
      turtle.goto(-262.5, -115.8)
      turtle.pendown()
      turtle.circle(16.15, -180)  #酱汁
      turtle.circle(-16.15, -180)
      turtle.circle(16.15, -180)
      turtle.circle(-16.15, -180)
      turtle.circle(16.15, -180)
      turtle.circle(-16.15, -180)
      turtle.circle(16.15, -180)
      turtle.circle(-16.15, -180)
      turtle.circle(16.15, -180)
      turtle.circle(-16.15, -180)
      turtle.circle(16.15, -180)
      turtle.circle(-16.15, -180)
      turtle.circle(16.15, -180)
      turtle.circle(-16.15, -180)
      turtle.circle(16.15, -180)
      turtle.circle(-16.15, -180)
      turtle.penup()
      turtle.goto(-203.7, -77.5)   #第二层蛋糕框
      turtle.pendown()
      turtle.right(180)
      turtle.forward(82)
      turtle.right(90)
      turtle.forward(399)
      turtle.right(90)
      turtle.forward(82)
      turtle.right(90)
      turtle.forward(36.75)
      turtle.right(90)
      turtle.circle(42, 180)   #馅料
      turtle.right(90)
      turtle.forward(36.75)
      turtle.right(90)
      turtle.circle(47.25, 180)
      turtle.right(90)
      turtle.forward(36.75)
      turtle.right(90)
      turtle.circle(42, 180)
      turtle.penup()
      turtle.goto(-203.7, -18.7)
      turtle.pendown()
      turtle.circle(10, -180)    #酱汁
      turtle.circle(-10, -180)
      turtle.circle(10, -180)
      turtle.circle(-10, -180)
      turtle.circle(10, -180)
      turtle.circle(-10, -180)
      turtle.circle(10, -180)
      turtle.circle(-10, -180)
      turtle.circle(10, -180)
      turtle.circle(-10, -180)
      turtle.circle(10, -180)
      turtle.circle(-10, -180)
      turtle.circle(10, -180)
      turtle.circle(-10, -180)
      turtle.circle(10, -180)
      turtle.circle(-10, -180)
      turtle.circle(10, -180)
      turtle.circle(-10, -180)
      turtle.circle(10, -180)
      turtle.circle(-10, -180)
      turtle.penup()
      turtle.goto(-145, 5)  #第三层蛋糕框
      turtle.pendown()
      turtle.right(180)
      turtle.forward(79.8)
      turtle.right(90)
      turtle.forward(279.3)
      turtle.right(90)
      turtle.forward(79.8)
      turtle.right(90)
      turtle.forward(42)
      turtle.circle(-21, 360)  #馅料
      turtle.forward(98)
      turtle.circle(-21, 360)
      turtle.forward(98)
      turtle.circle(-21, 360)
      turtle.penup()
      turtle.goto(-145, 63.8)
      turtle.pendown()
      turtle.left(90)
      turtle.circle(10, -180)  #酱汁
      turtle.circle(-10, -180)
      turtle.circle(10, -180)
      turtle.circle(-10, -180)
      turtle.circle(10, -180)
      turtle.circle(-10, -180)
      turtle.circle(10, -180)
      turtle.circle(-10, -180)
      turtle.circle(10, -180)
      turtle.circle(-10, -180)
      turtle.circle(10, -180)
      turtle.circle(-10, -180)
      turtle.circle(10, -180)
      turtle.circle(-10, -180)
      turtle.penup()
      turtle.goto(-102, 84.5)  #蜡烛
      turtle.pendown()
      turtle.right(180)
      turtle.forward(84)
      turtle.right(90)
      turtle.forward(21)
      turtle.left(45)  
      turtle.circle(10, 124)
      turtle.left(45)
      turtle.circle(10, 126)
      turtle.left(20)
      turtle.forward(21)
      turtle.right(90)
      turtle.forward(84)
      turtle.left(90)
      turtle.forward(42)
      turtle.left(90)
      turtle.forward(101)
      turtle.right(90)
      turtle.forward(21)
      turtle.left(45)  #
      turtle.circle(10, 124)
      turtle.left(45)
      turtle.circle(10, 126)
      turtle.left(20)
      turtle.forward(21)
      turtle.right(90)
      turtle.forward(99)
      turtle.left(90)
      turtle.forward(42)
      turtle.left(90)
      turtle.forward(84)
      turtle.right(90)
      turtle.forward(21)
      turtle.left(45)  #
      turtle.circle(10, 124)
      turtle.left(45)
      turtle.circle(10, 126)
      turtle.left(20)
      turtle.forward(21)
      turtle.right(90)
      turtle.forward(84)
      turtle.penup()
      turtle.goto(-102, 126.5)
      turtle.pendown()
      turtle.left(112.5)
      turtle.forward(42)
      turtle.penup()
      turtle.goto(-102, 105.5)
      turtle.pendown()
      turtle.forward(42)
      turtle.penup()
      turtle.goto(-20, 137)
      turtle.pendown()
      turtle.forward(42)
      turtle.penup()
      turtle.goto(-20, 111)
      turtle.pendown()
      turtle.forward(42)
      turtle.penup()
      turtle.goto(60, 126.5)
      turtle.pendown()
      turtle.forward(42)
      turtle.penup()
      turtle.goto(60, 105.5)
      turtle.pendown()
      turtle.forward(42)
      turtle.hideturtle()
    draw_cake()  
    
    mb.showinfo("哦耶~完成！", "对了{}，告诉您一件事。。。".format(name))
    def msg_box() :
       mb.showinfo("🎉🎉🎉", "{}, {}岁生日快乐！".format(name, age))
       
       if mb.askyesno("生日惊喜", "这里还有一份给{}的惊喜，是否查看？".format(name)):
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        
        # 等待 5 秒钟后弹出消息框
        time.sleep(5)
        mb.showinfo("生日惊喜", "哈哈，你被rick了！")
    window.ontimer(msg_box, 3000)
    
    
    
     # 运行窗口
    turtle.mainloop()
else:
    message = "非常抱歉，今天不是{}的生日哦！".format(name)

# 显示消息框
mb.showinfo(title="提示", message=message)