lists = ['a', 'v', 'sad', 'eae']

for item in lists:
    print(f"{item} is ma favorite")

print("I like food")

anis = ['dog', 'cat', 'bird']
for ani in anis:
    print(f"{ani} is an animal")

print("they are animal")

# a is ma favorite
# v is ma favorite
# sad is ma favorite
# eae is ma favorite
# I like food
# dog is an animal
# cat is an animal
# bird is an animal
# they are animal

for i in range(1,21):
    print(i)

lists = [23, 435, 45, 67, 13]
print(min(lists))
print(max(lists))
print(sum(lists))

lists = list(range(1,20,2))
print(lists) #[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

l2 = [val*3 for val in range(3,30)]
for i in l2:
    print(i)

l3 = [val**3 for val in range(1, 11)]
print(l3) #[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

l4 = [1,2,3,4,5,6,7]
print(l4[:4]) #[1, 2, 3, 4]
print(l4[-3:]) #[5, 6, 7]
print(l4[1:6:2]) #[2, 4, 6]
print(l4[1:5:2]) #[2, 4]

l5 = list(range(1,7,2))
print(l5) #[1, 3, 5]
l6 = l5[:] #this is for list copy,
print(l6) #[1, 3, 5]
l7 = l5 # &l7 = &l5
l5.append(123)
l6.append(123)
l7.append(123)
print(l5) #[1, 3, 5, 123, 123]
print(l6) #[1, 3, 5, 123]
print(l7) #[1, 3, 5, 123, 123]

tuple_1 = (1,2,3,4,5)
#tuple_1[0] = 1, error, cannot change tuple element

for i in tuple_1:
    print(i)

tuple_1 = (1,2,3)
print(tuple_1) #(1, 2, 3)

