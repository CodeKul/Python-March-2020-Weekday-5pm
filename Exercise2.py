'''
Write a Python function to print the even numbers from a given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9] 
Expected Result : [2, 4, 6, 8]
'''

def even_list(lst):
    ret_lst = []
    for ele in lst:
        if ele % 2 == 0:
            ret_lst.append(ele)
    return ret_lst


l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
l2 = even_list(l1)

print(l2)