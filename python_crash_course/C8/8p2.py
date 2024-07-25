def func1(*names):
    for name in names:
        print(f"name is {name}.")

def func2(**int_string):
    for key in int_string.keys():
        print(f"key {key} has value: {int_string[key]}. ")


l_names = ['aa', 'bb', 'cc']
func1('aa', 'bb', 'cc')

map_1 = {2:'apple', 1:'pear', 0:'orange'}
func2(a='apple', b='pear', c='orange')
# key a has value: apple. 
# key b has value: pear. 
# key c has value: orange.

def func3(**dic):
    dic['a'] = 2
    dic['c'] = 3
    return dic

ret = func3(a = 1, b = 11)
print(ret)
# {'a': 2, 'b': 11, 'c': 3}


    
