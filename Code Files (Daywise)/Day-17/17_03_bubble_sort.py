# bubble sort


# [ 1, 3, 4, 2, 5, 10, 6] => [1, 2, 3, 4, 5, 6, 10]
    #  1 3 2 4 5 6 10    => 1 time
    #                   =  2 time
    #                   ..
    #                   ...


  
ls = [ 9, 8, 7, 6, 5, 4, 3 ]

def bubble(ls):
    n = len(ls)

    for j in range(n):

        for i in range(0, n - j):
            if i+ 1 < n and ls[i] > ls[i+1]:
                ls[i], ls[i+1] = ls[i+1], ls[i]

        print(ls)

bubble(ls)

print("sorted")
print(ls)




