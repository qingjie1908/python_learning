dic1 = {2:7, 1:3, 3:6}
print(dic1[1]) #3

dic1[4] = 11
print(dic1) #{2: 7, 1: 3, 3: 6, 4: 11}

dic1[2] = dic1[2] + 1
print(dic1) #{2: 8, 1: 3, 3: 6, 4: 11}

del dic1[1]
print(dic1) #{2: 8, 3: 6, 4: 11}

print(dic1.get(1, -1)) #-1
print(dic1.get(2, -1)) #8

for key,value in dic1.items():
    print(f"key {key} has value: {value}")
# key 2 has value: 8
# key 3 has value: 6
# key 4 has value: 11

for key in dic1.keys():
    print(f"key is : {key}")
# key is : 2
# key is : 3
# key is : 4

for key in dic1:
    print(f"key is : {key}")
# key is : 2
# key is : 3
# key is : 4

dic2 = {2:7, 1:3, 3:6}
for key in sorted(dic2):
    print(f"key is : {key}")
# key is : 1
# key is : 2
# key is : 3

print(dic2) #{2: 7, 1: 3, 3: 6}

dic3 = {2:7, 1:3, 3:6, 4:7}
for value in set(dic3.values()): #build a set, remove duplicates
    print(value)
# 3
# 6
# 7

#build a set use {}
set1 = {3, 6, 7, 7}
print(set1) #{3, 6, 7}