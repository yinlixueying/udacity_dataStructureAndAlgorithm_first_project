#!/usr/bin/env python
# coding: utf-8

# In[18]:


import hashlib
import datetime


# In[25]:


def calc_hash(self):
      sha = hashlib.sha256()

      hash_str = "We are going to encode this string of data!".encode('utf-8')

      sha.update(hash_str)

      return sha.hexdigest()


# In[30]:


class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = calc_hash(str(data))
      self.previous_block = None
    def __str__(self):
        return str(self.timestamp)+" "+str(self.data)+" "+str( self.previous_hash)+" "+str( self.hash)


# In[35]:


class BlockChain:
    
    def __init__(self):
        self.head = None;
        
    def append(self, data, previous_hash):
        time = datetime.datetime.utcnow()
        if self.head == None:
            self.head = Block(time, data,0);
            return
        
        newHead = Block(time, data, previous_hash)
        newHead.previous_block = self.head
        self.head = newHead
    
    def to_list(self):
        BlockList = []
        
        block = self.head;
        while block:
            BlockList.append(block)
            block = block.previous_block
        return BlockList
    
    def size(self):
        size = 0
        block = self.head
        while block:
            size += 1
            block = block.previous_block
        return size;


# In[32]:


"""
# Test case 1
# Description: empty block
"""
test_case1 = BlockChain()
print("test case 1 \n")
print("test case 1 size:", test_case1.size())


# In[33]:


"""
# Test case 2
# Description: one block
"""
test_case2 = BlockChain()
test_case2.append("no",0);
print("test case 2, one block \n")
print("test case 2 size:", test_case2.size())
for item in test_case2.to_list():
    print(item)


# In[36]:


"""
# Test case 3
# Description: five block
"""
test_case3 = BlockChain()
test_case3.append("description",0);
test_case3.append("hardware",calc_hash("description"));
test_case3.append("nand",calc_hash("hardware"));
test_case3.append("command",calc_hash("nand"));
test_case3.append("ECU",calc_hash("command"));
print("test case 3, five block \n")
print("test case 3 size:", test_case3.size())
for item in test_case3.to_list():
    print(item)


# In[ ]:




