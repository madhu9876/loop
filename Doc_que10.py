n=int(input('enter your no'))
i=1
sum=0
while i<=n:
    if i%n==0:
        sum+=1
    i+=1
if sum==2:
	print('prime number')
else:
	print('not prime number')