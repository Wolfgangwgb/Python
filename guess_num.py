# -*- coding: utf-8 -*-
import tkinter as tk
import sys
import random
import re

number = random.randint(0,1024) #随机数
running = True
num = 0
nmaxn = 1024
nminn = 0
 #退出事件处理程序
def eBtnClose(event):
     root.destroy()
    
 #猜数字事件处理程序	
def eBtnGuess(event):
     global nmaxn
     global nminn
     global num
     global running

     if running:
         val_a = int(entry_a.get())#entry_a.get()获取文本中的内容
         if val_a == number:
             labelqval("恭喜答对了！")
             num+=1
             running = False
             numGuess()
         elif val_a < number:
             if val_a > nminn:
                 nminn = val_a
                 num+=1
                 label_tip_min.config(label_tip_min,text=nminn)
             labelqval("小了哦")
         else:
             if val_a < nmaxn:
                 nmaxn = val_a
                 num+=1
                 label_tip_max.config(label_tip_max,text=nmaxn)
             labelqval("大了哦")
     else:
         labelqval('你已经答对啦...')

def numGuess():
     if num == 1:
         labelqval('我靠！一次答对！')   
     elif num < 10:
         labelqval('十次以内就答对了牛逼。。尝试次数：'+str(num))
     elif num < 50:
         labelqval('还行哦尝试次数：'+str(num))
     else:
         labelqval('好吧。。。。。您都试了超过50次了。。。。尝试次数：'+str(num))
  
#设置标签内容函数  
def labelqval(vText):
     label_val_q.config(label_val_q,text=vText)   
 
# 主窗口
root = tk.Tk()
root.title("比大小游戏")
root.geometry("400x80+400+200")
 
 #最大/小值框架
line_a_tip = tk.Frame(root)  
#标签
label_tip_max = tk.Label(line_a_tip,fg="blue",text=nmaxn)
label_tip_min = tk.Label(line_a_tip,fg="blue",text=nminn)
#布局
label_tip_max.pack(side = "top",fill = "x")
label_tip_min.pack(side = "bottom",fill = "x")
line_a_tip.pack(side = "left",fill = "y")
 #顶部标签框架
line_question = tk.Frame(root)
label_val_q = tk.Label(line_question,fg="red",width="80")
label_val_q.pack(side = "left")
line_question.pack(side = "top",fill = "x")
 
 #文本输入框架
line_input = tk.Frame(root)
entry_a = tk.Entry(line_input,width="50")#entry单行文本框
#btnGuess = tk.Button(line_input,bg="yellow",text="猜")
entry_a.pack(side = "left")
#绑定事件处理程序
entry_a.bind('<Return>',eBtnGuess)
#btnGuess.bind('<Button-1>',eBtnGuess)
#btnGuess.pack(side = "left")
line_input.pack(side = "top",fill = "x")#fill 在x方向填充满
 
 
line_btn = tk.Frame(root,)
btnClose = tk.Button(line_btn,bg="green",text="退出")
btnClose.bind('<Button-1>',eBtnClose)
btnClose.pack(side="right",padx=50)
line_btn.pack(side = "top")

btnGuess = tk.Button(line_btn,bg="yellow",text="猜猜")
btnGuess.bind('<Button-1>',eBtnGuess)
btnGuess.pack(side = "left",padx=0)


labelqval("请输入0到1024之间任意整数：")
#entry_a.focus_set()
 
print(number)
root.mainloop()#主事件循环
