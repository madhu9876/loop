i=1
sum=0
while i<=11:
	n=int(input('enter your no'))
	sum=sum+i
	i=i+1
	a=sum/11
	print('sum=','sum','averge',a)
if i%5==0:
	print('divisible')
else:
    print('not divisible')