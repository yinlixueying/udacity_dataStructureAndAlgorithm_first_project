#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Rearrange Array Elements so as to form two number such that their sum is maximum. 
Return these two numbers. You can assume that all array elements are in the range [0, 9]. 
The number of digits in both the numbers cannot differ by more than 1. 
You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be [542, 31]. 
In scenarios such as these when there are more than one possible answers, return any one.
"""


# In[1]:


def mergesort(items):

    if len(items) <= 1:
        return items
    
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    
    left = mergesort(left)
    right = mergesort(right)
    
    return merge(left, right)
    
def merge(left, right):
    
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
        
    return merged


# In[23]:


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if(len(input_list) == 0):
        return (-1, -1)
    if(len(input_list) == 1):
        return(input_list[0], 0)
    input_list = mergesort(input_list)
    input_list.reverse()
    num1 = ""
    num2 = ""
    i = 0
    while(i <= (len(input_list) - 1)):
        if(i % 2 == 0):
            num1 += str(input_list[i])
        else:
            num2 += str(input_list[i])
        i += 1
    return(int(num1), int(num2))


# In[28]:


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function([[], [-1, -1]])
test_function([[9], [9, 0]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])


# In[25]:


"""
Pass
Pass
Pass
Pass
"""


# In[26]:





# In[27]:





# In[ ]:




