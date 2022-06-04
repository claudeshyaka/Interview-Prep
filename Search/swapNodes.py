# Swap nodes
from collections import deque

# Node class
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Swap tree nodes function.
def swapNodes(indexes, queries):
    # Insert node in tree using level order traversal
    def insert(root, indexes):
        q = deque([root])
        for x, y in indexes:
            temp = q.popleft()
            if x != -1:
                temp.left = Node(x)
                q.append(temp.left)
            if y != -1:
                temp.right = Node(y)
                q.append(temp.right)
        return root
    
    # create root node
    root = Node(1)
    # insert child nodes and return root node
    root = insert(root, indexes)
    
    # swap function
    def swap(root, k, level, l):
        if root:
            if level%k == 0:
                root.left, root.right = root.right, root.left
        
        swap(root.left, k, level+1, l)
        l.append(root.value)
        swap(root.right, k, level+1, l)
    
    result = []
    for k in queries:
        l = []
        swap(root, k, 1, l)
        result.append(l) 
    return result

# Driver code
indexes = [2, 3, -1, -1, -1, -1]
queries = [1, 1]
swapNodes(indexes, queries)