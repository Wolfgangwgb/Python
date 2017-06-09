
from tkinter import *


root = Tk()#创建主窗口对象

root.title('计算器')#窗口标题

root.geometry("300x400-0+0")#设置窗口大小及位置

#c = Canvas(root,width=300,height=200,bg='white')#创建画布对象

#c.pack()#使画布在窗口中显示

#c['bg'] ='green'#更改画布的颜色

#aLabel.pack()



def ISP(ch):
	if ch == "(":
		return 6
	elif ch in ["*","%","/"]
		return 4
	elif ch in ["-","+"]
		return 2
	elif ch == ")"
		return 1
	elif ch == "#"
		return 0
	
def ICP(ch):
	if ch == "(":
		return 1
	elif ch in ["*","%","/"]
		return 5
	elif ch in ["-","+"]
		return 3
	elif ch == ")"
		return 6
	elif ch == "#"
		return 0

		
stack = [#]
print(stack)


def MidtoLast():
	global s
	global s1
	while():
		i=0
		if s[i] in ['(','+','-','*','/','%',')','#']:
			if ICP(s[i])>ISP(stack[-1]):	
				stack.append(s[i])
				i++
				continue
			elif ICP(s[i])<ISP(stack[-1]):
				s1+=s[i]
				s.pop()
				continue
			else:
				if stack[-1] == "(":
					i++
					s.pop()
					continue
				
		else:
			s1+=s[i]
	



s = ''
#响应函数
def show1():
	global s
	s+='1'
	aLabel.config(None,justify ="left",text=s)
		
def show2():
	global s
	s+='2'
	aLabel.config(None,justify ="left",text=s)

def show3():
	global s
	s+='3'
	aLabel.config(None,justify ="left",text=s)

def show4():
	global s
	s+='4'
	aLabel.config(None,justify ="left",text=s)

def show5():
	global s
	s+='5'
	aLabel.config(None,justify ="left",text=s)

def show6():
	global s
	s+='6'
	aLabel.config(None,justify ="left",text=s)

def show7():
	global s
	s+='7'
	aLabel.config(None,justify ="left",text=s)

def show8():
	global s
	s+='8'
	aLabel.config(None,justify ="left",text=s)

def show9():
	global s
	s+='9'
	aLabel.config(None,justify ="left",text=s)
def show0():
	global s
	s+='0'
	aLabel.config(None,justify ="left",text=s)

def showadd():
	global s
	s+='+'
	aLabel.config(None,justify ="left",text=s)
def showsub():
	global s
	s+='-'
	aLabel.config(None,justify ="left",text=s)
def showcul():
	global s
	s+='*'
	aLabel.config(None,justify ="left",text=s)
def showchu():
	global s
	s+='/'
	aLabel.config(None,justify ="left",text=s)
def showquyu():
	global s
	s+='%'
	aLabel.config(None,justify ="left",text=s)
def showequal():
	global s
	s+='/'
	aLabel.config(None,justify ="left",text=s)
	
def showleftk():
	global s
	s+='('
	aLabel.config(None,justify="left",text=s)
	
def showrightk():
	global s
	s+=')'
	aLabel.config(None,justify="left",text=s)
	
def showclear():
	global s
	s=""
	aLabel.config(None,text=s)
aLabel = Label(root,bg="white",fg="black",state="disable",justify ="left",height=1,width= 41,text="文国邦")


#定义按钮
Btn1 = Button(root,text="1",width = 4,command= show1)
Btn2 = Button(root,text="2",width = 4,command= show2)
Btn3 = Button(root,text="3",width = 4,command= show3)
Btn4 = Button(root,text="4",width = 4,command= show4)
Btn5 = Button(root,text="5",width = 4,command= show5)
Btn6 = Button(root,text="6",width = 4,command= show6)
Btn7 = Button(root,text="7",width = 4,command= show7)
Btn8 = Button(root,text="8",width = 4,command= show8)
Btn9 = Button(root,text="9",width = 4,command= show9)
Btn0 = Button(root,text="0",width =4,command = show0)

Btnadd = Button(root,text="+",width = 4,command= showadd)
Btnsub = Button(root,text="-",width = 4,command= showsub)
Btncul = Button(root,text="*",width = 4,command= showcul)
Btnchu = Button(root,text="/",width = 4,command= showchu)
Btnquyu = Button(root,text="%",width = 4,command= showquyu)
Btnequal = Button(root,text="=",width = 4,command= showequal)

Btnclear = Button(root,text="<-",width = 4,command= showclear)
Btnclear.place(x=210,y=100)
Btnleftk = Button(root,text="(",width = 4,command= showleftk)
Btnleftk.place(x=210,y=150)

Btnrightk = Button(root,text=")",width = 4,command= showrightk)
Btnrightk.place(x=210,y=200)
#按钮布局
Btn1.place(x=10,y=100)
Btn2.place(x=60,y=100)
Btn3.place(x=110,y=100)
Btn4.place(x=10,y=150)
Btn5.place(x=60,y=150)
Btn6.place(x=110,y=150)
Btn7.place(x=10,y=200)
Btn8.place(x=60,y=200)
Btn9.place(x=110,y=200)
Btn0.place(x=60,y=250)

Btnadd.place(x=160,y=100)
Btnsub.place(x=160,y=150)
Btncul.place(x=160,y=200)
Btnchu.place(x=160,y=250)
Btnequal.place(x=110,y=250)
Btnquyu.place(x=10,y=250)

aLabel.place(x=3,y=70)


root.mainloop()


