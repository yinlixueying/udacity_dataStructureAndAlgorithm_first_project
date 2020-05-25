#!/usr/bin/env python
# coding: utf-8

# In[25]:


import os


# In[31]:


def find_files(suffix,path):
    if path == None:
        return None
    if suffic == None:
        return None
    fileList = [];
    for item in os.listdir(path):
        joinedPath = os.path.join(path, item);
        if(os.listdir(joinedPath)):
            fileList += find_files(suffix,joinedPath)
        elif(os.path.isfile(joinedPath) and joinedName.endswith(suffix)):
            fileList.append(item);
    return fileList;


# In[ ]:




