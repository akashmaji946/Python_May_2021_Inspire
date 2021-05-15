



# n! = n * n-1 * n-2 ....1

# n = 4

# ans = 1
# for i in range(1, n):
# 	ans += i*ans
# print(ans)

def factorial(n):
	ans = 1
	for i in range(1, n):
		ans += i*ans
	print(ans)

factorial(5)


# DSA (data structures & algorithms)
