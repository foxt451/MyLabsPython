y0 = 1
y = (y0 + 1) / (y0 + 2)
eps = 1E-5
while abs(y - y0) >= eps:
    y0 = y
    y = (y0 + 1) / (y0 + 2)
print("y =", y)
