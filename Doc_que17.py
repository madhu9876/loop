i=int(input("Enter any number"))
arm=i
sum=0
while i>0:
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
if arm==sum:
   	print('number is armstrong')
else:
    print('number is not armstrog')