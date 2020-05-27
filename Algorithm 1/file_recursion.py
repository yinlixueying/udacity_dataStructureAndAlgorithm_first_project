#!/usr/bin/env python
# coding: utf-8

# In[25]:


import os


# In[31]:


def find_files(suffix,path):
    if path == None:
        return None
    if suffix == None:
        return None
    fileList = [];
    dir_list= os.listdir(path)
    for item in dir_list:
        joinedPath = os.path.join(path, item);
        
        if(os.path.isfile(joinedPath) and joinedPath.endswith(suffix)):
            fileList.append(item);
        elif(os.path.isdir(joinedPath)):
            fileList += find_files(suffix,joinedPath)
    return fileList;


def find_files_walk(suffix, path = None):
    path_list = []
    for dirpath, dirnames, files in os.walk(path):
        for name in files:
            if name.endswith(suffix):
                path_list.append(os.path.join(dirpath, name))
    return path_list

# In[ ]:
print("****Empty test directory****")        
print(find_files(".c", "E:/Udacity/testdir/subdir6"))
print(find_files_walk(".c", "E:/Udacity/testdir/subdir6"))
print("****No files ending in .c test no_c_dir****")        
print(find_files(".c", "E:/Udacity/testdir/subdir4"))
print(find_files_walk(".c", "E:/Udacity/testdir/subdir4"))
print("****Single file ending in .c test c_dir****")        
print(find_files(".py", "E:/Udacity"))
print(find_files_walk(".py", "E:/Udacity"))
print()
print("****Udacity supplied test directory****")        
print(find_files(".c", "E:/Udacity/testdir/"))
print(find_files_walk(".c", "E:/Udacity/testdir/"))

"""
****Empty test directory****
[]
[]
****No files ending in .c test no_c_dir****
[]
[]
****Single file ending in .c test c_dir****
['active directory.py', 'blockChain.py', 'file_recursion.py', 'huffman coding.py', 'huffman_coding.py', 'LRU.py', 'union_and_intersection_of_two_linkedLists.py']
['E:/Udacity\\active directory.py', 'E:/Udacity\\blockChain.py', 'E:/Udacity\\file_recursion.py', 'E:/Udacity\\huffman coding.py', 'E:/Udacity\\huffman_coding.py', 'E:/Udacity\\LRU.py', 'E:/Udacity\\union_and_intersection_of_two_linkedLists.py']

****Udacity supplied test directory****
['a.c', 'b.c', 'a.c', 't1.c']
['E:/Udacity/testdir/t1.c', 'E:/Udacity/testdir/subdir1\\a.c', 'E:/Udacity/testdir/subdir3\\subsubdir1\\b.c', 'E:/Udacity/testdir/subdir5\\a.c']
"""



