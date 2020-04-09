'''
    if condition:
        true statements
    else:
        false statements
'''

a = 11
b = 20

'''
if a < b:
    print("a is less than b")
elif a == b:
    print("a and b both are equal")
else:
    print("a is greater than b")
    print("This is another line")
'''

if a < b:
    print("a is less than b")
    if a == 10:
        print("a is equal to 10")
else:
    if a == b:
        print("a and b both are equal")
    else:
        print("a is greater than b")


# Loop
'''
    initialisation
    while condition:
        statements
        incr/decr

'''

i = 0
while i < 10:
    if i % 2 == 0:
        print("{} - Codekul".format(i))
        i += 1
        continue
    else:
        print("{} - The Gurukul for Coders!".format(i))
        break
    i += 1

i = 0
while i < 5:
    j = 0
    while j < 5:
        print("i: {} j: {}".format(i, j))
        j += 1
    i += 1

'''
    for item in collection:
        statements
'''

for ch in "Codekul":
    print(ch)

l1 = [34, 46, 12, 67, 38, 27]

sum = 0
for num in l1:
    sum += num # sum = sum + num

print("Sum:", sum)