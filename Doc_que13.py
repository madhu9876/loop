num=int(input("Enter any number"))
reversed_num=0
while num!=0:
    digit=num%10
    reversed_num=reversed_num*10+digit
    num=num//10
    print("reversed num:"+ 'str', (reversed_num))
num=num+1