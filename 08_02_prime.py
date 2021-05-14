

# 2 factors
# 12 => >2 (no)
# 7 => 1, 7 (yes)

factors = 0

n = 100

# factor = factor + 1   
for i in range(1, n+1):
	if n % i == 0:
		factors += 1
print(factors)

if factors == 2:
	print("Prime")
else:
	print("Not prime")
