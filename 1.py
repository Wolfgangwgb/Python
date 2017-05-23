

#print('200+300=',200+300)


#a=input('请输入\n')
#print(a)


#idx1 = input('Please input\n')
#idx2 = idx1
#print(idx1)
#type(idx1)
##print('\n')
#print(idx2)
#type(idx2)

#for i in range(1,10,2):
#	print(i)
#import sys
#j=4	
#while j<5:
#	print(j)
#	j-=1
#	if(j == 0):
#		sys.exit()

for i in range(1,10):
	for j in range(1,i+1):
		print('%d * %d = %d'%(i,j,i*j),end='  ') #print函数默认结尾换行，关键字参数通常用于可选变元，print函数有两个可选变元end和sep
		#end = '' : 末尾打印什么
		#sep = ',' :参数之间打印什么
		j+=1
	print('\n')

	








