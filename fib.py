print "Fibonacci Series"
x = input("Enter the number of terms in the series\n")
a = 1
b = 1
fiblist = []
print a,"\n",b
for c in range(1,x-1):
	sum1 = a + b
	fiblist[c] = sum1
	a=b
	b=sum1
print fiblist