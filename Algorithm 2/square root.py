#!/usr/bin/env python
# coding: utf-8

# In[5]:


def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    l = 0
    r = number
    ans = -1
    if number == 0:
        return 0
    if number < 0:
        return None;
    while(l <= r):
        median = (l + r)//2
        if(median * median <=  number):
            ans = median
            l = median + 1
        else:
            r = median - 1
    return ans


# In[6]:


print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (None == sqrt(-1)) else "Fail")


# In[ ]:




