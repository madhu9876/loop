i=1
while i<=100:
	if i%3==0:
		print('Nav')
	if i%7==0:
		print('Gurukul')
	if i%3==0 and i%7==0:
		print('NavGurukul')
	else:
		print(i)
	i=i+1