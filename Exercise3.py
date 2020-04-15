'''
Write a Python program that accepts a string and calculate the number of digits and letters.
Sample Data : Python 3.2
Expected Output :
Letters 6 
Digits 2
'''

s1 = input('Enter a string: ')
cnt_ltr = 0
cnt_num = 0
for ch in s1:
    if ch.isdigit():
        cnt_num += 1
    elif ch.isalpha():
        cnt_ltr += 1

print('Letters:',cnt_ltr)
print('Numbers:',cnt_num)
