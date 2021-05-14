
# factors of a number

# 7 => 1, 7
# 12 => 1, 2, 3, 4, 6, 12

# n => 1, 2, 3, ....., n-1, n

# n = 15
# 1.....n(include)
n = 15
for i in range(1, n+1):
	if n % i == 0:
		print(i, end = " ")




