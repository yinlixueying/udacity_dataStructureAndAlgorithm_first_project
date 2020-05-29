#!/usr/bin/env python
# coding: utf-8

# In[54]:


"""
HTTPRouter using a Trie
For this exercise we are going to implement an HTTPRouter like you would find in a typical web server using the Trie data structure we learned previously.

There are many different implementations of HTTP Routers such as regular expressions or simple string matching, but the Trie is an excellent and very efficient data structure for this purpose.

The purpose of an HTTP Router is to take a URL path like "/", "/about", or "/blog/2019-01-15/my-awesome-blog-post" and figure out what content to return. In a dynamic web server, the content will often come from a block of code called a handler.


First we need to implement a slightly different Trie than the one we used for autocomplete. Instead of simple words the Trie will contain a part of the http path at each node, building from the root node /

In addition to a path though, we need to know which function will handle the http request. In a real router we would probably pass an instance of a class like Python's SimpleHTTPRequestHandler which would be responsible for handling requests to that path. For the sake of simplicity we will just use a string that we can print out to ensure we got the right handler

We could split the path into letters similar to how we did the autocomplete Trie, but this would result in a Trie with a very large number of nodes and lengthy traversals if we have a lot of pages on our site. A more sensible way to split things would be on the parts of the path that are separated by slashes ("/"). A Trie with a single path entry of: "/about/me" would look like:

(root, None) -> ("about", None) -> ("me", "About Me handler")

We can also simplify our RouteTrie a bit by excluding the suffixes method and the endOfWord property on RouteTrieNodes. We really just need to insert and find nodes, and if a RouteTrieNode is not a leaf node, it won't have a handler which is fine.
"""
# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler=None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)
    
    def insert(self, path_names, end_handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        if path_names == None:
            return None
        
        current_node = self.root
        for name in path_names:
            current_node.insert(name, None);
            current_node = current_node.children[name];
        current_node.handler = end_handler
        
    def find(self, path_names):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        if len(path_names) == 0:
            return self.root.handler
        current_node = self.root;
        
        for name in path_names:
            if name not in current_node.children:
                return None
            else:
                current_node = current_node.children[name]
        return current_node.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler        
        self.handler = handler
        self.children = {}

    def insert(self, value, handler):
        # Insert the node as before
        if value not in self.children:
            self.children[value] = RouteTrieNode()
            self.children[value].handler = handler

        


# In[55]:


# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, handler, error_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.root= RouteTrie(handler)
        self.errorHandler = error_handler

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_list = self.split_path(path)
        root_node = self.root
        root_node.insert(path_list, handler)
        

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        
        path_list = self.split_path(path)

        find_result = self.root.find(path_list)
        if find_result == None:
            return self.errorHandler
        else:
            return find_result


    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        if path == "/":
            return []
        path_list = path.split('/')
        path_list.remove('')
        return path_list


# In[56]:


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this  , 
router.add_handler("/home/about", "about handler")  # add a route


# In[57]:


# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one


# In[ ]:




