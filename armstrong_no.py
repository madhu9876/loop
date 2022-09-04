# num=int(input("enter the check num:"))
# i=num
# count=0
# while i>0:
#     count=count+1
#     i=i//10
# sum=0
# i=num
# while i>0:
#     rem=i%10
#     x=1
#     product=1
#     while x<=count:
#         product=product*rem
#         x=x+1
#     sum=sum+product
#     i=i//10
# if sum==num:
#     print("armstrong number")
# else:
#     print("not armstrong number")


# 
# Armstrong100se 1000
a = 100
b = 1000
for num in range(a,b+ 1):
   order = len(str(num))
   sum = 0
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10
   if num == sum:
       print(num)