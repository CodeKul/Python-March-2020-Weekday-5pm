# Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included).

def square_list(st, ed):
    for element in range(st, ed+1):
        print(element ** 2)

square_list(1, 30)