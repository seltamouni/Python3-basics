'''
def my_func():
	x = 10
	print("Value inside function:",x)

x = 20
my_func()
print("Value outside function:",x)
'''
'''
4 types of arguments

-required
-keyword
-default
-variable lenght

'''


def sum(x=0,y=0):
    return(x+y)
s = sum(3,7)
print(s)
print(sum())
