num=int(input("Enter any number"))
p=1
while num!=0:
   r=num%10
   p=p*r
   num=num//10
print("Product of digits is",p)