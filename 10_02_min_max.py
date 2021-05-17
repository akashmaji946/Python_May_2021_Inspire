
# loops


l = [9, 3, 2, -1]
# mv = 9

# li = 9  mv 
# li = 3  mv = 3
# li = 2  mv = 2 
# li = -1  mv = -1 

# n elems => 0.......n-1
# None => nothing
# 0 -> first elem pos
# 0 based indexed lang.
min_val = l[0]
for i in range(0, len(l)):
	if l[i] < min_val:
		min_val = l[i]
print(min_val)


max_val = l[0]
for i in range(0, len(l)):
	if l[i] > max_val:
		max_val = l[i]
print(max_val)


