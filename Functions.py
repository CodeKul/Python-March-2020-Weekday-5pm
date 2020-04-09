def my_function():
    print("This is my function!")

my_function()

def function_with(param1, param2):
    print("This is param1: ", param1)
    print("This is param2: ", param2)

function_with("Codekul", "Python")

def function_with_default(a, b, c, d=10):
    print("a:", a)    
    print("b:", b)
    print("c:", c)
    print("d:", d)

function_with_default(1, 2, 3, 4)

def function_returning():
    str1 = "Codekul"
    return str1

str2 = function_returning()
print(str2)

def change_var(var):
    var = 10
    print('var:',var)

var1 = 100
change_var(var1)
print('var1:',var1)

def change_list(l1):
    # l1.append(5)
    l1 = [1,2,3,4,5]
    print('l1:', l1)

l2 = [1,2,3,4]
change_list(l2)
print("l2:", l2)