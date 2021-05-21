def heron(n, e = 0.0001):
   
    prev = 0
    curr = n

    while True:

        prev = curr
        curr = (curr + n/curr) * 0.5
    

        if abs(prev - curr) <= e:
            print(prev, ans)
            break

    return prev

n = 25
ans = heron(n)
print("Square root of {0} is {1:0.2f}".format(n, ans))



print("Geeks : %2d, Portal : %5.2f" % (1, 05.333))