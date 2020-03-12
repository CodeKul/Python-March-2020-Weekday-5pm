# str 

str1 = "Codekul"
str2 = 'Codekul'

# "Codekul" - 'The Gurukul For Coders'!
str3 = '''"Codekul" - 'The Gurukul For Coders'!'''
print(str3)

str4 = """ABC
    DEF
        GHI"""
print(str4)

a = 10
b = 20
# a: 10 b: 20
print("a: %d b: %d %s" %(a, b, str1))

print("a: {} b: {} {}".format(a, b, str1))

print(str3.find("u"))


# List

list1 = [1,2,3,4,5, 'Six', 7.8, True, False]
print(list1)
print(type(list1))
print(len(list1))

list1.append(10)
print(list1.count(7.8))
print(list1)

list2 = [10,4,35,3,56, 21]
list2.sort()
print(list2)


# Tuple

tup1 = (1, 2, 3, 4, 5)
print(tup1[4])
print(type(tup1))

# tup1.append(10)
print(tup1)


# Dict

dict1 = {"key1": "value1", "key2": "value2", "key3": "value3"}

dict2 = {"One": 1, "Two": 2, 3: "Three"}
print(dict2["Two"])