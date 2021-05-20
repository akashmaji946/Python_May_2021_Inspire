# A simple example of an algorithm
# Linear Search

# [1, 3, 4, 6, 7, 9, 10]   => 5   (yes/no)


#linear-search-algo
#input -> list, num
#output-> True/False

ls = [1, 3, 4, 6, 7, 9, 10]
num = 6

#snake case
def linear_search(ls, num):
  # check for the num in ls
  for n in ls:
    if n == num:
      return True
  # num nhi mila
  return False

ans = linear_search(ls, num)
print(ans)


# two things
# size of input (ls size)
# space memory (constant)



  



