#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
# Union and Intersection of Two Linked Lists
# Your task for this problem is to fill out the union and intersection functions. 
# The union of two sets A and B is the set of elements which are in A, in B, 
# or in both A and B. The intersection of two sets A and B, denoted by A ∩ B, 
# is the set of all objects that are members of both the sets A and B.
#
# You will take in two linked lists and return a linked list that is composed of either the union or intersection, respectively. 
# Once you have completed the problem you will create your own test cases and perform your own run time analysis on the code.
#
# We have provided a code template below, you are not required to use it:
"""


# In[5]:


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


# In[16]:


def union(llist_1, llist_2):
    # Your Solution Here
    itemList = [];
    unions = LinkedList()
       #Return None if both linked lists are empty
    if llist_1.head is None and llist_2.head is None:
        return None

    A_head = llist_1.head;
    while (A_head is not None):
        if A_head.value not in itemList:
            itemList.append(A_head.value)
        A_head = A_head.next
    B_head = llist_2.head;
    while (B_head is not None):
        if B_head.value not in itemList:
            itemList.append(B_head.value)
        B_head = B_head.next

    for item in itemList:
        unions.append(item)
    return unions


# In[25]:


def intersection(llist_1, llist_2):
    # Your Solution Here
    itemList = [];
    itemSet = set()
    unions = LinkedList()
       #Return None if both linked lists are empty
    if llist_1.head is None and llist_2.head is None:
        return None
    A_head = llist_1.head;
    while (A_head is not None):
        if A_head.value not in itemList:
            itemList.append(A_head.value)
        A_head = A_head.next
    B_head = llist_2.head;
    while (B_head is not None):
        if B_head.value in itemList:
            itemSet.add(B_head.value)
        B_head = B_head.next
    if len(itemSet) == 0:
        return None
    for item in itemSet:
        unions.append(item)
    return unions


# In[26]:


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(linked_list_1)
print(linked_list_2)
print("Union")
print (union(linked_list_1,linked_list_2))
print("Intersection")
print (intersection(linked_list_1,linked_list_2))


# In[ ]:


"""
case 1:
3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 6 -> 4 -> 3 -> 21 -> 
6 -> 32 -> 4 -> 9 -> 6 -> 1 -> 11 -> 21 -> 1 -> 
Union
3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11 -> 
Intersection
4 -> 21 -> 6 -> 
"""


# In[27]:


# Test case 2
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(linked_list_3)
print(linked_list_4)
print("Union")
print (union(linked_list_3,linked_list_4))
print("Intersection")
print (intersection(linked_list_3,linked_list_4))


# In[28]:


"""
case 2
3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 6 -> 4 -> 3 -> 23 -> 
1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 1 -> 
Union
3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 
Intersection
None
"""


# In[29]:


#Test case 3
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]

for i in element_1:
    linked_list_5.append(i)
    
print(linked_list_5)
print("Empty List")
print("Union")
print (union(linked_list_5,linked_list_6))
print("Intersection")
print (intersection(linked_list_5,linked_list_6))


# In[ ]:


"""
case 3
3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 6 -> 4 -> 3 -> 23 -> 
Empty List
Union
3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 
Intersection
None
"""


# In[30]:


#Test case 4
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()
    
print("Empty List 1")
print("Empty List 2")
print("Union")
print (union(linked_list_7,linked_list_8))
print("Intersection")
print (intersection(linked_list_7,linked_list_8))


# In[ ]:


"""
Empty List 1
Empty List 2
Union
None
Intersection
None
"""

