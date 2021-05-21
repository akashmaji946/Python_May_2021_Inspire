# anagram

#  abcc  -> cbac
# yes

# defd => dedg
# no

# racecar
# r 0
# a 0
# c 0
# e 0

# acercar

# dictionary

string1 = "aeiou"
string2 = "aeiok"

map = {}
for ch in string1:
    if ch in map:
        map[ch] += 1
    else:
        map[ch] = 1
print(map)



for ch in string2:
    if ch in map:
        map[ch] -= 1


# kya map me sare values 0 hain ?
anagram = True

for key in map:
    if map[key] != 0:
        anagram = False
        break
    
print(map)
print(anagram)







    





