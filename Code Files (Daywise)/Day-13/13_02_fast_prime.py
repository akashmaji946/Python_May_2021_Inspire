# fast prime check
# input: n = 13
# out: true/false

# n => 1, n   => 2 factors

# 36   => 1, 2, 3, 4, 6, 9, 12, 18, 36
# 36 => 6
# 17 => 1, 17

# 2 -> 4   => 2  3  4

# 1   36/1   36
# 2   36/2   18
# 3   36/3   12


def fast_prime_check(n):
  # 1.....n
  # 2......(n**0.5)
  for i in range(2, int(n**0.5)):
    if n%i == 0:
      return False

  return True


print(fast_prime_check(42))

# 2.......sqrt(n) # fast
# n = 100 => 10 steps


