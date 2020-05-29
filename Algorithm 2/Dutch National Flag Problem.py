#!/usr/bin/env python
# coding: utf-8

# In[10]:


"""
Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.

Note: O(n) does not necessarily mean single-traversal. For e.g. if you traverse the array twice, that would still be an O(n) solution but it will not count as single traversal.

Here is some boilerplate code and test cases to start with:
"""
def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    if input_list == None:
        return None
    if(input_list == []):
        return []
    start = 0
    pointer = 0
    end = len(input_list) - 1
    midNum = 1
    while(pointer <= end):
        if(input_list[pointer] < midNum):
            temp = input_list[start]
            input_list[start] = input_list[pointer]
            input_list[pointer] = temp
            start += 1
            pointer += 1
        elif(input_list[pointer] > midNum):
            temp = input_list[pointer]
            input_list[pointer] = input_list[end]
            input_list[end] = temp
            end -= 1
        else:
            pointer += 1
    return input_list


# In[12]:


def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == None:
        print(sorted_array)
        print("Pass")
        return
    if sorted_array == []:
        print(sorted_array)
        print("Pass")
        return
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function(None)       
test_function([])
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])


# In[ ]:


"""
None
Pass
[]
Pass
[0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]
Pass
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
Pass
[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
Pass
"""

