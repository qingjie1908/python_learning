mlist = [6, 8, 1, 2, 5]

print(mlist) #[6, 8, 1, 2, 5]

print(sorted(mlist)) #[1, 2, 5, 6, 8]

print(mlist) #[6, 8, 1, 2, 5]

mlist.reverse() 

print(mlist) #[5, 2, 1, 8, 6]

mlist.reverse()

print(mlist) #[6, 8, 1, 2, 5]

mlist.sort()

print(mlist) #[1, 2, 5, 6, 8]

mlist.sort(reverse=True) 

print(mlist) #[8, 6, 5, 2, 1]