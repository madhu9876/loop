num=int(input("Enter any number"))
k=str(num)
i=0
sum=0
while i<len(k):
   digit=num%10
   num=num//10
   sum=sum+digit*2**i
   i=i+1

print(sum)