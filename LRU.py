#!/usr/bin/env python
# coding: utf-8

# In[16]:


from collections import OrderedDict
class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.cache = OrderedDict()
        pass

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
        else:
            value = -1
        return value

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value;
        else:
            if len(self.cache)==self.capacity:
                self.cache.popitem(last=False);
                self.cache[key] = value
            else:
                self.cache[key] = value


# In[17]:


our_cache = LRU_Cache(5)


# In[18]:


our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


# In[19]:


our_cache.get(1)       # returns 1


# In[20]:


our_cache.get(2)       # returns 2


# In[21]:


our_cache.get(9)      # returns -1 because 9 is not present in the cache


# In[22]:


our_cache.set(5, 5) 
our_cache.set(6, 6)

our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry


# In[ ]:




