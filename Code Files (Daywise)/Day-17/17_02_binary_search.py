
#  binary search

# array (list) => already sorted
# search = 15

# l = [1, 4, 7, 9, 10, 11, 15, 20, 34] 
                    # s    m,e

# s, e, m                

   #  m = (s + e)//2


# friends = ["rakesh", "anuj", "mohit", ......]

elem = 34
ls = [1, 4, 7, 9, 10, 11, 15, 20, 34] 
                                  
    
def binary_search(ls, elem):

    s = 0
    e = len(ls) - 1

    while True:
        m = (s + e)//2

        # m => middle point

        if ls[m] == elem:
            return True
        elif ls[m] < elem:
            s = m + 1
        else:
            e = m - 1

        if s > e:
            return False

        

print(binary_search(ls, elem))

        





