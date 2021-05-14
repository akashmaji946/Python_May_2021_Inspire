


# 1, 2, 3, 4, .... 15

# i % 3   => "fizz"
# i % 5   => "buzz"

# i % 3   and  i % 5   => "fizzbuzz"

# i                    => i  

n = 15
for i in range(1, n+1):
	if i%3 == 0 and i%5 == 0:
		print("fizzbuzz")
	
	if i%3 == 0:
		print("fizz")
	elif i%5 == 0:
		print("buzz")
	
	
	else:
		print(i)
