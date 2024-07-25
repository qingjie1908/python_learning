def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user('Qingjie') #Hello, Qingjie!

def printlist1(listname): 
    listname.pop()
    print(listname)

l1 = [1,2,3,4,5,6]
printlist1(l1) #[1, 2, 3, 4, 5] 
print(l1) #[1, 2, 3, 4, 5] #will change original list

printlist1(l1[:]) #copy assignment, [1, 2, 3, 4], not change orig list
print(l1) #[1, 2, 3, 4, 5]
