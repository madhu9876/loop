# n=int(input('enter your no'))
# count=0
# i=1
# while i<=n:
# 	if n%i==0:
# 	    count=count+1
# 	i=i+1
# if count==2:
# 	print('prime no',n)
# else:
# 	print("not prime no",n)


# Prime no 1to100
Number=1
while(Number <= 100):
    count = 0
    i = 2
    
    while(i <= Number//2):
        if(Number % i == 0):
            count = count + 1
            break
        i = i + 1
    if (count == 0 and Number != 1):
        print(" %d" %Number, end = '  ')
    Number = Number  + 1