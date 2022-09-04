# a=(input("enter string:"))
# b=a[-1::-1]
# if a==b:
#     print("string palindrome ")
# else:
#     print("not string palindrome")
    
    
num=int(input("enter the number:"))
ornum=num
rn=0
while num>0:
    rem=num%10
    rn=rn*10+rem
    num=num//10
if ornum==rn:
    print("number is  palindrome ")
else:
    print("number is not palindrome")   