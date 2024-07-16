guests = ['a', 'b', 's', 'c']

for p in guests:
    print(f"{p} is comming to dinner.")

# a is comming to dinner.
# b is comming to dinner.
# s is comming to dinner.
# c is comming to dinner.

guests.remove('a')
print(guests) #['b', 's', 'c']

guests.append('g') #['b', 's', 'c', 'g']
print(guests)

guests.insert(0, 'x') #['x', 'b', 's', 'c', 'g']
print(guests)

guests.insert(int(len(guests)/2), 'tr') #['x', 'b', 'tr', 's', 'c', 'g']
print(guests)

guests.append('4tq3') #['x', 'b', 'tr', 's', 'c', 'g', '4tq3']
print(guests)

while(len(guests) > 2):
    pop_name = guests.pop()
    print(f"{pop_name} is out.")
# 4tq3 is out.
# g is out.
# c is out.
# s is out.
# tr is out.

print(guests) #['x', 'b']

del guests[0]
print(guests) #['b']

del guests[0] #[]
print(guests)
