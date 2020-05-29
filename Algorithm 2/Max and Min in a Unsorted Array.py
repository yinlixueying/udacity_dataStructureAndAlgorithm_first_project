#!/usr/bin/env python
# coding: utf-8

# In[16]:


"""
In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.

Bonus Challenge: Is it possible to find the max and min in a single traversal?
"""
def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if(ints == None or ints == []):
        return None
    if(len(ints)==1):
        return (ints[0], ints[0])
    
    min = ints[0]
    max = ints[0]
    for i in range(1, len(ints)-1):
        if ints[i] < min:
            min = ints[i]
        elif ints[i] > max:
            max = ints[i]
    return(min, max)


# In[17]:



import random

"""
Example Test Case of null list
"""
l = None

print ("Pass" if (None == get_min_max(l)) else "Fail")

# Example Test Case of One Interger
l = [1] 

print ("Pass" if ((1,1) == get_min_max(l)) else "Fail")

## Example Test Case of Ten Integers
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

"""
Example Test Case of 100,000 Integers
"""
l = [i for i in range(0, 100000)]  # a list containing 0 - 99999
random.shuffle(l)

print ("Pass" if ((0, 99999) == get_min_max(l)) else "Fail")


# In[3]:


"""
Pass
Pass
Pass
Pass
"""


# In[5]:





# In[6]:





# In[ ]:




