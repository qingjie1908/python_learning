name = input("please enter user name: ")
print(name)

age = input("how old are you? ")
print(age)

#print(age+1), error, age is string, input get string

age = int(age) #change to int
print(age) #21
print(age+1) #22

print(4 % 2) #0
print(4 % 3) #1

a = 1
while (a <= 5):
    print(a)
    a += 1

l1 = [1,2,3,3,4,3,5]

while 3 in l1:
    l1.remove(3)
print(l1) #[1, 2, 4, 5]