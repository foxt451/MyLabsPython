x = int(input("Enter x: "))
if x <= -1:
	y = 1 / x ** 2
elif x <= 2:
	y = x ** 2
else:
	y = 4
print("f(x) = ", y)
