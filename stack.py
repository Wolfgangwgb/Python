
##创建栈
#s =[]
##push操作
#s.append(1)
#s.append(2)
#
##size操作
#print(len(s))
#
#print(s)
##pop 操作
#s.pop()
#print(s)
#s.append(12)
##获取栈顶元素
#print(s[-1]) #列表的负数下标
#
#print(not s)

#括号匹配
#1.创建栈，保存未匹配的左括号
#2.遍历字符串，(1)如果是左括号入栈，
			  #(2)如果是右括号,如果栈空，则右括号多；否则取栈顶元素判断与右括号是不是匹配，
#3.遍历完如果栈空，匹配正确，否则左括号多			  

left = {'{','[','('}
right = {'}',']',')'}

def match(Str):
	s = []
	for c in Str:
		if c in left:
			s.append(c)
		elif c in right:	
			if not s:
				print('右括号多')
				return   #直接返回
			elif (c is ')'and s[-1] is '(' )or (c is ']' and s[-1] is '[') or (c is '}' and s[-1] is '{'):
				s.pop()
				continue
			else: 
				print('括号次序匹配不正确')
				return
	
	if not s:
		print('括号匹配正确')
	else:
		print('左括号多')
		
Str = input()
match(Str)

		
		
		
		
		
		
		
		