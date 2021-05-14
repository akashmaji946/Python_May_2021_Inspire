
# leap year program

# year = 2020

# % 4 => leap
# % 400 =>leap
# %100 => not leap year

# 2000 => 400 (leap)
# 1700 => 400 X    100  (not leap)
# 2004 => 4 (leap)
# 1231 => not leap

year = 1900

if year % 400 == 0:
	print("leap")
elif year % 100 == 0:
	print("not leap")
elif year % 4 == 0:
	print("leap")
else:
	print("not leap")

