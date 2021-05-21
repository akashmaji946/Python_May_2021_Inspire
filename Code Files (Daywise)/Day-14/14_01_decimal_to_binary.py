# decimal -> binary

# 12   => 1100

# 10 =>   1010
# 8 =>   1000

# 8   8/2   0
# 4   4/2   0
# 2   2/2   0
# 1   1/2   1
# 0    (stop)

n = 100
ls = []
while n != 0:
    if n % 2 == 0:
        ls.append(0)
    else:
        ls.append(1)
    n = n//2 #integer  9//2   4  (not 4.5)

for i in ls[::-1]:
    print(i, end = " ")


# string = "akash"
# print(string[::-1])


# string[::-1]     #complete string in reverse

    


