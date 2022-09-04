num=int(input("enter the num:"))
sum=0
temp=num
while temp>0:
    fac=1
    i=1
    rem=temp%10
    while i<=rem:
        fac=fac*i
        i=i+1
    sum=sum+fac
    temp=temp//10
if sum==num:
    print("strong number",num)
else:
    print("not stron number",num)