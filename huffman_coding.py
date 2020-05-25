#!/usr/bin/env python
# coding: utf-8

# In[83]:


import sys
import heapq


# In[98]:


class huffman_Node(object):
    def __init__(self, value, freq):
        self.left = None;
        self.right = None;
        self.value = value;
        self.freq = freq;
    def __lt__(self, node):
        return self.freq < node.freq;
    def __str__(self):
        return str(self.value)+" "+str(self.freq)


# In[99]:


def get_frequency(str):
    freq = {};
    for i in str:
        if i in freq:
            freq[i] += 1;
        else:
            freq[i] = 1;
    sorted_freq = sorted(zip(freq.values(), freq.keys()));
    for i in range(len(sorted_freq)):
        value = sorted_freq[i][1]; #second item is value
        freq = sorted_freq[i][0]; #first item is frequency     
        sorted_freq[i] = huffman_Node(value, freq);
    return sorted_freq;


# In[100]:


def huffman_tree(data):
    heap = get_frequency(data);
    heapq.heapify(heap);
    while(len(heap) != 1):
        treeNode = huffman_Node(None,None);
        treeLeft = heapq.heappop(heap);
        treeNode.left = treeLeft;
        treeRight = heapq.heappop(heap);
        treeNode.right = treeRight;
        treeNode.freq = treeLeft.freq + treeRight.freq;
        heapq.heappush(heap, treeNode);
    return heap;


# In[101]:


def huffcode_table(root):
    code = {};
    def getCode(sNode, curCode=""):
        if(sNode == None):
            return;
        if(sNode.left == None and sNode.right == None):
            code[sNode.value] = curCode;
        getCode(sNode.left, curCode + "0");
        getCode(sNode.right, curCode + "1");
    getCode(root[0]);
    return code;


# In[102]:


def huffman_encoding(data):
    if(len(get_frequency(data)) == 1):
        return "0" * len(data);
    if(len(data) == 0):
        return "";
    huffmanCode = "";
    root = huffman_tree(data);
    table = huffcode_table(root);
    for item in data:
        huffmanCode += table[item];
    return huffmanCode, huffman_tree(data);


# In[107]:


def huffman_decoding(data,tree):
    if(len(get_frequency(data))== 1):
        return len(data)* str(tree.value);
    decodeString = "";
    dataLength = len(data);
    count = 0;
    while(count < dataLength):
        start = tree[0];
        while(start.left != None and start.right != None):
            if(data[count] == "0"):
                start = start.left;
            else:
                start = start.right;
            count += 1;
        decodeString += str(start.value);
    return decodeString;


# In[108]:


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))


# In[ ]:




